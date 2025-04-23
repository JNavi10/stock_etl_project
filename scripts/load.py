# scripts/load.py

import os
from datetime import datetime

def load(df):
    filename = f"/tmp/ohlc_{datetime.today().date()}.csv"
    df.to_csv(filename, index=False)
    return filename
