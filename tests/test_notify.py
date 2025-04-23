import pandas as pd
from scripts.notify import notify_anomalies

def test_notify_skips_if_no_anomalies():
    df = pd.DataFrame({
        "Ticker": ["AAPL"],
        "Open": [100],
        "Close": [101],
        "% Change": [0.01],
        "Anomaly": [False]
    })
    result = notify_anomalies(df, "x@y.com", "x@y.com", "fakepass", dry_run=True)
    assert result == False

def test_notify_detects_anomalies():
    df = pd.DataFrame({
        "Ticker": ["AAPL"],
        "Open": [100],
        "Close": [106],
        "% Change": [0.06],
        "Anomaly": [True]
    })
    result = notify_anomalies(df, "x@y.com", "x@y.com", "fakepass", dry_run=True)
    assert result == True
