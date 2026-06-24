import requests
import pandas as pd

from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://fashion-studio.dicoding.dev/"


def scrape_page(page):
    """
    Scrape satu halaman website
    """

    try:

        if page == 1:
            url = BASE_URL
        else:
            url = f"{BASE_URL}page{page}"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return BeautifulSoup(response.text, "html.parser")

    except requests.exceptions.RequestException as e:
        print(f"Error scraping page {page}: {e}")
        return None


def extract_products(soup):
    """
    Ambil seluruh produk dalam satu halaman
    """

    products = []

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cards = soup.find_all("div", class_="collection-card")

    for card in cards:

        try:

            title = card.find(
                "h3",
                class_="product-title"
            ).text.strip()

            price = card.find(
                class_="price"
            ).text.strip()

            p_tags = card.find_all("p")

            rating = p_tags[0].text.strip()
            colors = p_tags[1].text.strip()
            size = p_tags[2].text.strip()
            gender = p_tags[3].text.strip()

            products.append(
                {
                    "Title": title,
                    "Price": price,
                    "Rating": rating,
                    "Colors": colors,
                    "Size": size,
                    "Gender": gender,
                    "timestamp": timestamp,
                }
            )

        except Exception as e:
            print(f"Error parsing product: {e}")

    return products


def scrape_all():
    """
    Scrape halaman 1-50
    """

    all_products = []

    for page in range(1, 51):

        print(f"Scraping page {page}")

        soup = scrape_page(page)

        if soup is None:
            continue

        products = extract_products(soup)

        all_products.extend(products)

    df = pd.DataFrame(all_products)

    return df