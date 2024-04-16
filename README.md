# Real Estate Data Engineering Real Time Pipeline

![Contributors](https://img.shields.io/github/contributors/drjodyannjones/RealEstateDataEngineering.svg?style=for-the-badge)
![Forks](https://img.shields.io/github/forks/drjodyannjones/RealEstateDataEngineering.svg?style=for-the-badge)
![Stargazers](https://img.shields.io/github/stars/drjodyannjones/RealEstateDataEngineering.svg?style=for-the-badge)
![Issues](https://img.shields.io/github/issues/drjodyannjones/RealEstateDataEngineering.svg?style=for-the-badge)
![MIT License](https://img.shields.io/github/license/drjodyannjones/RealEstateDataEngineering.svg?style=for-the-badge)

## Introduction
This project builds a real-time data pipeline using Apache Kafka, Apache Spark, and Cassandra. Designed with scalability in mind, the system addresses the dynamic needs of the London real estate market. I leverage BrightData's web scraper with real-time data ingestion through an Apache Kafka producer. An Apache Spark cluster is set up as the consumer, which then outputs the data stream into CassandraDB, which acts as the sink in this pipeline. This pipeline delivers a high-performance, scalable solution for extracting, processing, and analyzing real-time property data from Zoopla. This project is tailored for data-driven decision-making, advanced analytics, and operational excellence in the real estate sector.

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



## Getting Started
To get a local copy up and running follow these simple steps:
```bash
git clone https://github.com/drjodyannjones/RealEstateDataEngineering.git
cd RealEstateDataEngineering
docker build -t real-estate-pipeline .
docker-compose up
```

## Usage
For running the Spark jobs and analyzing real estate data, use:
```bash
spark-submit --class your.class.path jobs/spark-job.py
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
