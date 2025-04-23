import pandas as pd
from datetime import datetime
from scripts.transform import transform

def test_transform_flags_anomaly_correctly():
    mock_data = {
        "AAPL": pd.DataFrame({
            "Open": [100.0],
            "Close": [106.0],  # +6%
            "High": [107.0],
            "Low": [99.0],
            "Volume": [7000000],
            "Date": [datetime.now()]
        })
    }

    result = transform(mock_data, tickers=["AAPL"])
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 1
    assert result.loc[0, "Anomaly"] == True

def test_transform_no_anomaly():
    mock_data = {
        "AAPL": pd.DataFrame({
            "Open": [100.0],
            "Close": [102.0],  # +2%
            "High": [103.0],
            "Low": [99.5],
            "Volume": [5000000],
            "Date": [datetime.now()]
        })
    }

    result = transform(mock_data, tickers=["AAPL"])
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 1
    assert result.loc[0, "Anomaly"] == False
