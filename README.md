# Real Estate Data Engineering Pipeline

## Run Spark job locally
```spark-submit --packages com.datastax.spark:spark-cassandra-connector_2.12:3.4.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1 spark-consumer.py```


## Build custom docker image using Dockerfile
```docker build -t my-custom-spark:3.5.0 .```


## Run Spark job on docker
```docker exec -it realestatedataengineering-spark-master-1 spark-submit \
    --packages com.datastax.spark:spark-cassandra-connector_2.12:3.4.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 \
    jobs/spark-consumer.py```

