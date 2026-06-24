import pandas as pd

USD_TO_IDR = 16000


def clean_price(price):

    if pd.isna(price):
        return None

    price = str(price).strip()

    if price == "Price Unavailable":
        return None

    try:
        price = price.replace("$", "")
        return float(price) * USD_TO_IDR
    except:
        return None


def clean_rating(rating):

    if pd.isna(rating):
        return None

    rating = str(rating)

    if "Invalid Rating" in rating:
        return None

    if "Not Rated" in rating:
        return None

    try:
        rating = (
            rating
            .replace("Rating:", "")
            .replace("⭐", "")
            .replace("/ 5", "")
            .strip()
        )

        return float(rating)

    except:
        return None


def clean_colors(colors):

    try:
        return int(
            str(colors)
            .replace("Colors", "")
            .strip()
        )
    except:
        return None


def clean_size(size):
    return str(size).replace("Size:", "").strip()


def clean_gender(gender):
    return str(gender).replace("Gender:", "").strip()


def transform_data(df):

    try:

        # buang Unknown Product dulu
        df = df[df["Title"] != "Unknown Product"]

        df["Price"] = df["Price"].apply(clean_price)
        df["Rating"] = df["Rating"].apply(clean_rating)
        df["Colors"] = df["Colors"].apply(clean_colors)
        df["Size"] = df["Size"].apply(clean_size)
        df["Gender"] = df["Gender"].apply(clean_gender)

        # buang baris yang gagal transform
        df = df.dropna()

        # hapus duplikat
        df = df.drop_duplicates()

        # pastikan tipe data
        df["Price"] = df["Price"].astype(float)
        df["Rating"] = df["Rating"].astype(float)
        df["Colors"] = df["Colors"].astype(int)

        return df

    except Exception as e:
        print(f"Transform Error: {e}")
        return pd.DataFrame()