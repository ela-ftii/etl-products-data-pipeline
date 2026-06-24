import pandas as pd

from utils.load import save_csv


def test_save_csv():

    df = pd.DataFrame(
        {
            "Title": ["Test Product"],
            "Price": [160000.0],
            "Rating": [4.5],
            "Colors": [3],
            "Size": ["M"],
            "Gender": ["Men"],
            "timestamp": ["2025-01-01"]
        }
    )

    save_csv(df, "test_output.csv")

    loaded = pd.read_csv("test_output.csv")

    assert len(loaded) == 1


def test_save_csv_error():

    # memicu except karena objek tidak punya to_csv()
    save_csv("bukan_dataframe", "error.csv")

    assert True