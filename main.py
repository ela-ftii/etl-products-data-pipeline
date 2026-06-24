from utils.extract import scrape_all
from utils.transform import transform_data
from utils.load import save_csv


def main():

    print("EXTRACT")
    raw_df = scrape_all()

    print(raw_df.shape)

    # Debug
    print(raw_df["Price"].unique()[:20])

    print("TRANSFORM")
    clean_df = transform_data(raw_df)

    print(clean_df.shape)
    print(clean_df.dtypes)

    print("LOAD")
    save_csv(clean_df)

    print("SELESAI")


if __name__ == "__main__":
    main()