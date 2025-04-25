import os
from datetime import datetime
from google.cloud import bigquery

def load_csv_to_bigquery():
    project_id = "stock-etl-project-457710"
    dataset_id = "stock_data"
    table_id = "ohlc_prices"
    bucket_name = os.getenv("GCS_BUCKET")
    bucket_path = f"gs://{bucket_name}/ohlc/ohlc_{datetime.today().date()}.csv"

    client = bigquery.Client(project=project_id)
    full_table_id = f"{project_id}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
    )

    load_job = client.load_table_from_uri(bucket_path, full_table_id, job_config=job_config)
    load_job.result()

    print(f"Successfully loaded data into {full_table_id}")
