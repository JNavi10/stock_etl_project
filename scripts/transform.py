# scripts/transform.py

import pandas as pd

ANOMALY_THRESHOLD = 0.05

def transform(raw_df, tickers):
    results = []
    for ticker in tickers:
        if ticker not in raw_df:
            continue
        df = raw_df[ticker].copy()
        df = df.reset_index()
        df["Ticker"] = ticker
        if len(df) == 0:
            continue
        df["% Change"] = (df["Close"] - df["Open"]) / df["Open"]
        df["Anomaly"] = (df["% Change"].abs() > ANOMALY_THRESHOLD)
        results.append(df)
    return pd.concat(results, ignore_index=True)
