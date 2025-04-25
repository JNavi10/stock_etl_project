# scripts/load.py

from datetime import datetime
from google.cloud import storage
import os

def load(df):
    filename = f"/tmp/ohlc_{datetime.today().date()}.csv"
    df.to_csv(filename, index=False)

    # Upload to GCS
    bucket_name = os.getenv("GCS_BUCKET")  # e.g. stock-etl-daily-exports
    destination_blob = f"ohlc/ohlc_{datetime.today().date()}.csv"

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob)
    blob.upload_from_filename(filename)

    print(f"[INFO] Uploaded to gs://{bucket_name}/{destination_blob}")
    return filename
