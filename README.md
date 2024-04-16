# Real Estate Data Engineering Real Time Pipeline

![Contributors](https://img.shields.io/github/contributors/drjodyannjones/RealEstateDataEngineering.svg?style=for-the-badge)
![Forks](https://img.shields.io/github/forks/drjodyannjones/RealEstateDataEngineering.svg?style=for-the-badge)
![Stargazers](https://img.shields.io/github/stars/drjodyannjones/RealEstateDataEngineering.svg?style=for-the-badge)
![Issues](https://img.shields.io/github/issues/drjodyannjones/RealEstateDataEngineering.svg?style=for-the-badge)
![MIT License](https://img.shields.io/github/license/drjodyannjones/RealEstateDataEngineering.svg?style=for-the-badge)

## Introduction

This project develops a real-time data pipeline to leverage insights from the London real estate market. The system integrates a suite of powerful technologies, including Apache Kafka, Apache Spark, and Cassandra.

The pipeline begins with real-time data collection from BrightData's web scraper, which feeds into an Apache Kafka producer. This architecture is engineered for maximum efficiency and scalability.

The data is then processed by an Apache Spark cluster and stored in a robust CassandraDB solution. A key innovation is the strategic integration of OpenAI's AI models, which significantly enhance the system's ability to extract, structure, and analyze property listings from Zoopla in real time.

This AI-powered integration not only improves the accuracy of the data extraction, but also provides greater flexibility in handling the information. As a result, stakeholders are empowered with actionable insights for swift decision-making.

Aimed at boosting operational efficiency and providing scalable solutions, this data pipeline is a cornerstone for advancing analytics and enhancing market responsiveness in the dynamic real estate sector.
## Built With
- **BrightData**: For real-time data scraping
- **Apache Spark**: For large-scale data processing
- **Docker**: For creating a consistent development and deployment environment
- **Python**: Primary programming language

## Project Structure
```
├── Dockerfile                          # Defines the Docker image for running the application environment.
├── README.md                           # Documentation for the project, setup, usage, and more.
├── config
│   └── config.json                     # Configuration settings (e.g., database connections, API keys).
├── docker-compose.yml                  # Docker Compose configuration for multi-container applications.
├── jobs
│   ├── requirements.txt                # Python dependencies for the Spark jobs.
│   └── spark-consumer.py               # Spark job script for processing real estate data.
├── main.py                             # Main Python script to initiate data processing jobs.
├── requirements.txt                    # Python dependencies required for the entire project.
```

## Prerequisites
- Docker
- Apache Spark 3.5.0
- Python 3.9
- Scala 2.12
- OpenAI API Key

## Getting Started
### Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/drjodyannjones/RealEstateDataEngineering.git
```


## Usage
1. Building Docker Image:
```bash
docker build -t my-custom-spark:3.5.0 .
```

2. Start Docker Container
```bash
docker compose up -d
```

3. Start Data Ingestion process:
```bash
python main.py
```
4. Start Spark Consumer:
```bash
docker exec -it realestatedataengineering-spark-master-1 spark-submit \
    --packages com.datastax.spark:spark-cassandra-connector_2.12:3.4.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 \
    jobs/spark-consumer.py
```

## Contributing
Contributions make the open source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements
- Yusuf Ganiyu, for his mentorship and invaluable insights. [Connect with Yusuf](https://www.linkedin.com/in/yusuf-ganiyu-b90140107/)
- BrightData

## Contact
Dr. Jody-Ann Jones - [drjodyannjones@gmail.com](mailto:drjodyannjones@gmail.com)
Project Link: [https://github.com/drjodyannjones/RealEstateDataEngineering](https://github.com/drjodyannjones/RealEstateDataEngineering)
