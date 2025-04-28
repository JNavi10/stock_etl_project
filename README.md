

# Stock ETL Pipeline

This project implements an **ETL pipeline** for extracting, transforming, and loading **stock market data**. The pipeline pulls data from an external source (Yahoo Finance API), transforms it, and loads it into **Google Cloud Storage (GCS)** and **BigQuery** for further analysis. The project is designed to automate the data extraction process and enable seamless storage in the cloud for future analysis and visualization.

## Purpose

The purpose of this project was to create an automated and scalable ETL pipeline that extracts stock market data for a specific day (one day prior), transforms the data for analysis, and stores it in **Google Cloud** services. This project serves as a foundation for automating stock data workflows, providing insights into stock trends, and simplifying further analysis with tools like **Google Looker Studio**.

## Technologies Used

- **Python 3.10**: Python is used as the primary programming language for the ETL process. It is chosen for its simplicity, readability, and rich ecosystem of libraries for data manipulation (such as **Pandas**).
  
- **Apache Airflow**: Airflow is used for orchestrating and scheduling the ETL tasks. It enables the automation and monitoring of the data pipeline, ensuring that tasks are executed in the correct order and on time.
  
- **Google Cloud Platform (GCP)**:
  - **Google Cloud Storage (GCS)**: Raw stock market data is stored in GCS. This cloud storage service is scalable, cost-effective, and reliable for storing large datasets.
  - **BigQuery**: Processed stock market data is loaded into BigQuery, which serves as the data warehouse for analysis and querying. BigQuery’s scalability and performance make it ideal for handling large volumes of data.
  - **Google Looker Studio**: Used to visualize and analyze the stock data in an interactive dashboard. Looker Studio allows users to create dynamic and customizable reports from the processed data stored in BigQuery.

- **Pandas**: Used for data transformation, cleaning, and manipulation. Pandas provides fast and efficient data structures, making it an ideal choice for working with tabular data.

- **Google Cloud Python Client**: The Python client is used to interact with Google Cloud services like GCS and BigQuery. This client library facilitates uploading data to GCS and loading data into BigQuery programmatically.

## Technical Details

- **Data Extraction**: The pipeline extracts stock market data for the previous day using an external API (Yahoo Finance). It pulls OHLC (Open, High, Low, Close) data for the stocks of interest.
  
- **Data Transformation**: The raw data is cleaned, processed, and transformed into a suitable format for analysis. The transformation process includes removing duplicates, handling missing values, and performing any necessary calculations or aggregations.

- **Data Loading**: The transformed data is loaded into both **Google Cloud Storage (GCS)** and **BigQuery**. GCS is used as a backup for raw data, while **BigQuery** serves as the data warehouse for processed data.

- **Scheduling and Orchestration**: Apache Airflow is used to schedule and orchestrate the entire ETL process. The pipeline runs on a daily schedule, extracting data for the previous day, transforming it, and loading it into GCS and BigQuery.

## Future Enhancements

- **Error Handling**: Improve error handling in the Airflow DAG to ensure more reliable retries and notifications in case of failures.
