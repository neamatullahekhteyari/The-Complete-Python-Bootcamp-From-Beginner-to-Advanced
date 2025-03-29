import requests
from bs4 import BeautifulSoup

BASE_URL = "http://quotes.toscrape.com"

def fetch_data(url):
    headers = {"User-Agent":"Mozila/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None

def parse_data(html):
    soup = BeautifulSoup(html, "html.parser")
    quotes_data = []

    for quote_block in soup.select('.quote'):
        quote =  quote_block.select_one('.text').text.strip()
        author = quote_block.select_one('.author').text.strip()
        quotes_data.append({"Quote": quote, "Author": author})

    return quotes_data

def scrape_all_pages():
    all_quotes = []
    page = 1

    while True:
        url = f"{BASE_URL}/page/{page}/"
        print(f"Scraping page {page}...")

        html_content = fetch_data(url)
        if not html_content:
            break

        quotes = parse_data(html_content)
        if not quotes:
            break

        all_quotes.extend(quotes)
        page += 1

    return all_quotes

