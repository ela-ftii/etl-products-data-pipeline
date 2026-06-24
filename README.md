# Product Catalog ETL Pipeline

An automated, modular, and fully-tested Data Pipeline built in Python to extract, transform, and load e-commerce product data into a production-ready structured format.

## Project Overview
This project establishes a reliable data ingestion pipeline that processes raw fashion and retail product metadata, enforces strict data validation and cleaning rules, and exports the clean dataset for further business analysis.

The pipeline executes three main operational phases:
- **Extract**: Dynamically crawls and scrapes raw product metadata (Titles, Prices, Ratings, Colors, Sizes, and Demographics) from catalog sources using `BeautifulSoup4`.
- **Transform**: Automatically standardizes currencies, converts pricing schemas, handles missing attributes, parses structured sizing data, and removes duplicates or data anomalies.
- **Load**: Safely writes and saves the refined dataset into a final production file (`products.csv`).

---

## Project Structure
```text
.
├── tests/                  # Automated Unit Testing Suites
│   ├── test_extract.py     # Extraction layer tests
│   ├── test_transform.py   # Data validation and cleaning tests
│   └── test_load.py        # Loading logic tests
├── utils/                  # Core Modular ETL Pipeline
│   ├── extract.py          # Web scraping modules
│   ├── transform.py        # Data type casting & cleaning logics
│   └── load.py             # CSV export management
├── main.py                 # Application Entry Point
├── products.csv            # Final Cleaned Output Dataset (Production-ready)
├── pytest.ini              # Testing Configurations
└── requirements.txt        # Third-party Dependencies
