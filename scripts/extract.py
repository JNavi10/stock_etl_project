# scripts/extract.py

import yfinance as yf
from datetime import datetime, timedelta

TICKERS = ["META", "AAPL", "PLTR"]

def extract():
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    df = yf.download(
        tickers=TICKERS,
        start=str(yesterday),
        end=str(today),
        interval="1d",
        group_by="ticker",
        auto_adjust=False,
        threads=True,
    )
    return df, TICKERS
