# scripts/load.py

from datetime import datetime
from google.cloud import storage
import os
from google.auth import default as google_auth_default
from google.auth.exceptions import DefaultCredentialsError

def load(df):
    today_str = str(datetime.today().date())
    filename = f"/tmp/ohlc_{today_str}.csv"

    print(f"[DEBUG] Saving DataFrame to local file: {filename}")
    df.to_csv(filename, index=False)

    # Check if file actually saved
    if os.path.exists(filename):
        print(f"[DEBUG] Local file created: {filename} (Size: {os.path.getsize(filename)} bytes)")
    else:
        raise FileNotFoundError(f"[ERROR] Failed to save CSV file: {filename}")
    
        # Check if credentials are available
    try:
        credentials, project = google_auth_default()
        print(f"[DEBUG] Google credentials found for project: {project}")
    except DefaultCredentialsError as e:
        raise EnvironmentError(f"[ERROR] Google credentials not found: {str(e)}")


    # Upload to GCS
    bucket_name = os.getenv("GCS_BUCKET")
    if not bucket_name:
        raise EnvironmentError("[ERROR] GCS_BUCKET environment variable is not set.")

    destination_blob = f"ohlc/ohlc_{today_str}.csv"

    print(f"[DEBUG] Uploading {filename} to GCS bucket '{bucket_name}' at '{destination_blob}'")

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob)
    blob.upload_from_filename(filename)

    print(f"[INFO] Uploaded successfully to gs://{bucket_name}/{destination_blob}")

    return filename
