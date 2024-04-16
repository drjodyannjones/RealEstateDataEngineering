import logging
from cassandra.cluster import Cluster
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, FloatType, ArrayType

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_cassandra_session():
    """Retrieve or create a Cassandra session."""
    if 'cassandra_session' not in globals():
        cluster = Cluster(["cassandra"])
        globals()['cassandra_session'] = cluster.connect()
    return globals()['cassandra_session']


def setup_cassandra(session):
    """Setup the keyspace and table in Cassandra."""
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS property_streams
        WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};
    """)
    logger.info("Keyspace created successfully!")

    session.execute("""
        CREATE TABLE IF NOT EXISTS property_streams.properties (
            price text, title text, link text, pictures list<text>, floor_plan text,
            address text, bedrooms text, bathrooms text, receptions text, epc_rating text,
            tenure text, time_remaining_on_lease text, service_charge text,
            council_tax_band text, ground_rent text, PRIMARY KEY (link)
        );
    """)
    logger.info("Table created successfully!")


def insert_data(**kwargs):
    """Insert data into Cassandra table using a session created at the executor."""
    session = get_cassandra_session()
    session.execute("""
        INSERT INTO property_streams.properties (
            price, title, link, pictures, floor_plan, address, bedrooms, bathrooms,
            receptions, epc_rating, tenure, time_remaining_on_lease, service_charge, council_tax_band, ground_rent
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        kwargs['price'], kwargs['title'], kwargs['link'], kwargs['pictures'],
        kwargs['floor_plan'], kwargs['address'], kwargs['bedrooms'], kwargs['bathrooms'],
        kwargs['receptions'], kwargs['epc_rating'], kwargs['tenure'], kwargs['time_remaining_on_lease'],
        kwargs['service_charge'], kwargs['council_tax_band'], kwargs['ground_rent']
    ))
    logger.info("Data inserted successfully!")



def define_kafka_to_cassandra_flow(spark):
    """Define data flow from Kafka to Cassandra using Spark."""
    schema = StructType([
        StructField("price", FloatType(), True),
        StructField("title", StringType(), True),
        StructField("link", StringType(), True),
        StructField("pictures", ArrayType(StringType()), True),
        StructField("floor_plan", StringType(), True),
        StructField("address", StringType(), True),
        StructField("bedrooms", StringType(), True),
        StructField("bathrooms", StringType(), True),
        StructField("receptions", StringType(), True),
        StructField("epc_rating", StringType(), True),
        StructField("tenure", StringType(), True),
        StructField("time_remaining_on_lease", StringType(), True),
        StructField("service_charge", StringType(), True),
        StructField("council_tax_band", StringType(), True),
        StructField("ground_rent", StringType(), True)
    ])

    kafka_df = (spark
                .readStream
                .format("kafka")
                .option("kafka.bootstrap.servers", "kafka-broker:9092")
                .option("subscribe", "properties")
                .option("startingOffsets", "earliest")
                .load()
                .selectExpr("CAST(value AS STRING) as value")
                .select(from_json(col("value"), schema).alias("data"))
                .select("data.*"))

    kafka_df.writeStream.foreachBatch(
        lambda batch_df, _: batch_df.foreach(
            lambda row: insert_data(**row.asDict())
        )
    ).start().awaitTermination()


def main():
    spark = SparkSession.builder.appName("RealEstateConsumer").config(
        "spark.cassandra.connection.host", "cassandra"
    ).config(
        "spark.jars.packages",
        "com.datastax.spark:spark-cassandra-connector_2.12:3.4.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0"
    ).getOrCreate()

    session = get_cassandra_session()
    setup_cassandra(session)
    define_kafka_to_cassandra_flow(spark)


if __name__ == "__main__":
    main()
