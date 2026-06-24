import pandas as pd

from utils.transform import (
    clean_price,
    clean_rating,
    clean_colors,
    clean_size,
    clean_gender,
    transform_data
)


def test_clean_price():
    assert clean_price("$10") == 160000.0


def test_clean_price_unavailable():
    assert clean_price("Price Unavailable") is None


def test_clean_price_nan():
    assert clean_price(None) is None


def test_clean_rating():
    assert clean_rating("Rating: ⭐ 4.5 / 5") == 4.5


def test_clean_rating_invalid():
    assert clean_rating("Rating: ⭐ Invalid Rating / 5") is None


def test_clean_rating_not_rated():
    assert clean_rating("Rating: Not Rated") is None


def test_clean_colors():
    assert clean_colors("3 Colors") == 3


def test_clean_colors_invalid():
    assert clean_colors(None) is None


def test_clean_size():
    assert clean_size("Size: XL") == "XL"


def test_clean_gender():
    assert clean_gender("Gender: Men") == "Men"


def test_transform_data():

    df = pd.DataFrame(
        {
            "Title": ["T-shirt"],
            "Price": ["$10"],
            "Rating": ["Rating: ⭐ 4.5 / 5"],
            "Colors": ["3 Colors"],
            "Size": ["Size: M"],
            "Gender": ["Gender: Men"],
            "timestamp": ["2025-01-01"]
        }
    )

    result = transform_data(df)

    assert not result.empty
    assert result["Price"].iloc[0] == 160000.0
    assert result["Rating"].iloc[0] == 4.5


def test_transform_data_error():

    # DataFrame salah supaya masuk except transform_data
    df = pd.DataFrame({"A": [1]})

    result = transform_data(df)

    assert result.empty