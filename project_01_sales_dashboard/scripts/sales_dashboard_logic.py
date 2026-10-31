import csv
import time
from pathlib import Path

from bs4 import BeautifulSoup
import requests


OUTPUT_PATH = Path(__file__).resolve().parent.parent / "outputs" / "market_data.csv"


def fetch_page(url):
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    return response.text


def extract_market_rows(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    rows = []

    for item in soup.select(".market-item"):
        product = item.select_one(".product-name")
        price = item.select_one(".price")

        if product and price:
            rows.append(
                {
                    "product": product.get_text(strip=True),
                    "price": price.get_text(strip=True),
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                }
            )

    return rows


def save_rows(rows):
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["product", "price", "timestamp"])
        writer.writeheader()
        writer.writerows(rows)


def main():
    sample_url = "https://example.com/market"
    html = fetch_page(sample_url)
    rows = extract_market_rows(html)
    save_rows(rows)
    print(f"Saved {len(rows)} records to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

