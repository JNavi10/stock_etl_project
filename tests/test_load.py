import pandas as pd
import os
from scripts.load_to_gcs import load

def test_load_saves_file():
    df = pd.DataFrame({"A": [1], "B": [2]})
    path = load(df)
    assert os.path.exists(path)
    os.remove(path)


import os
import pandas as pd
from datetime import datetime
from scripts.load_to_gcs import load

def test_load_creates_csv_file():
    # Prepare dummy DataFrame
    df = pd.DataFrame({
        "ticker": ["AAPL", "META"],
        "close": [172.5, 305.1],
    })

    # Call your real load function
    filename = load(df)

    # Step 1: Check if file was created
    assert os.path.exists(filename), f"File {filename} was not created."

    # Step 2: Optionally, read back and check content (optional, deeper check)
    loaded_df = pd.read_csv(filename)
    pd.testing.assert_frame_equal(loaded_df, df)

    # Step 3: Delete the file
    os.remove(filename)

    # Step 4: Confirm deletion
    assert not os.path.exists(filename), f"File {filename} was not deleted."