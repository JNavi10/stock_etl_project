# dags/stock_pipeline_dag.py

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import sys
import pandas as pd
from dotenv import load_dotenv

# Airflow container paths
sys.path.append("/opt/airflow")

# Import script logic
from scripts.extract import extract
from scripts.transform import transform
from scripts.load_to_gcs import load
from scripts.load_to_bigquery import load_csv_to_bigquery
from scripts.notify import notify_anomalies

# Load environment variables
load_dotenv()

# Credentials
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# File paths
RAW_PATH = "/tmp/raw.pkl"
TICKERS_PATH = "/tmp/tickers.txt"
TRANSFORMED_PATH = "/tmp/transformed.pkl"

# Step 1: Extract
def extract_task(**kwargs):
    raw_df, tickers = extract()
    raw_df.to_pickle(RAW_PATH)
    with open(TICKERS_PATH, "w") as f:
        f.write(",".join(tickers))

# Step 2: Transform
def transform_task(**kwargs):
    raw_df = pd.read_pickle(RAW_PATH)
    with open(TICKERS_PATH) as f:
        tickers = f.read().split(",")
    transformed_df = transform(raw_df, tickers)
    transformed_df.to_pickle(TRANSFORMED_PATH)

# Step 3: Load to GCS
def load_task(**kwargs):
    df = pd.read_pickle(TRANSFORMED_PATH)
    load(df)

# Step 4: Load to BigQuery
def load_bq_task(**kwargs):
    load_csv_to_bigquery()

# Step 5: Notify
def notify_task(**kwargs):
    df = pd.read_pickle(TRANSFORMED_PATH)
    notify_anomalies(df, EMAIL_SENDER, EMAIL_RECIPIENT, EMAIL_PASSWORD)

# DAG configuration
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='stock_pipeline_dag',
    default_args=default_args,
    description='Daily stock ETL pipeline with anomaly notifications and BigQuery load',
    schedule_interval='0 7 * * *',
    start_date=datetime(2024, 1, 1),
    catchup=False
)

# Task Definitions
extract_op = PythonOperator(
    task_id='extract',
    python_callable=extract_task,
    dag=dag
)

transform_op = PythonOperator(
    task_id='transform',
    python_callable=transform_task,
    dag=dag
)

load_op = PythonOperator(
    task_id='load_to_gcs',
    python_callable=load_task,
    dag=dag
)

load_bq_op = PythonOperator(
    task_id='load_to_bigquery',
    python_callable=load_bq_task,
    dag=dag
)

notify_op = PythonOperator(
    task_id='notify',
    python_callable=notify_task,
    dag=dag
)

# Task Execution Order
_ = extract_op >> transform_op >> load_op >> load_bq_op >> notify_op
