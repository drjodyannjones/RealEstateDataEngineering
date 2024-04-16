import logging
from cassandra.cluster import Cluster
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType


def main():
    logging.basicConfig(level=logging.INFO)

    spark = (SparkSession.builder.appName("RealEstateConsumer")
             .config("spark.cassandra.connection.host", "localhost")
             .config("spark.jar.packages", "com.datastax.spark:spark-cassandra-connector_2.13:3.4.1,"
                                           "org.apache.spark:spark-sql-kafka-0-10_2.13:3.4.1")
             .getOrCreate()
             )
    # Connect to Kafka
    kafka_df = (spark.readStream.format("kafka")
                .option("kafka.bootstrap.servers", "localhost:9092")
                .option("subscribe", "properties")
                .option("startingOffsets", "earliest")
                .load())

    schema = StructType([
        StructField("price", FloatType(), True),
        StructField("title", StringType(), True),
        StructField("link", StringType(), True),
        StructField("pictures", StringType(), True),
        StructField("floor_plan", StringType(), True),
        StructField("address", StringType(), True),
        StructField("bedrooms", IntegerType(), True),
        StructField("bathrooms", IntegerType(), True),
        StructField("receptions", IntegerType(), True),
        StructField("tenure", StringType(), True),
        StructField("time_remaining_on_lease", IntegerType(), True),
        StructField("service_charge", FloatType(), True),
        StructField("council_tax_band", StringType(), True),
        StructField("ground_rent", FloatType(), True)
    ])


if __name__ == "__main__":
    main()
