FROM apache/airflow:2.8.1-python3.10

USER airflow

RUN pip install --user --upgrade pip && \
    pip install --user yfinance pandas python-dotenv google-cloud-storage google-cloud-bigquery pandas-market-calendars
