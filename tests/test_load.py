import pandas as pd
import os
from scripts.load import load

def test_load_saves_file():
    df = pd.DataFrame({"A": [1], "B": [2]})
    path = load(df)
    assert os.path.exists(path)
    os.remove(path)
