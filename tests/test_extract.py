from utils.extract import (
    scrape_page,
    extract_products,
    scrape_all
)


def test_scrape_page():
    soup = scrape_page(1)
    assert soup is not None


def test_extract_products():
    soup = scrape_page(1)

    products = extract_products(soup)

    assert len(products) > 0
    assert isinstance(products, list)


def test_scrape_all():
    df = scrape_all()

    assert not df.empty
    assert "Title" in df.columns