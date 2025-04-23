from scripts.extract import extract
import pandas as pd

def test_extract_output():
    df, tickers = extract()
    assert isinstance(tickers, list)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
