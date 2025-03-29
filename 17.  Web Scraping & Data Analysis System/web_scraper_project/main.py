from scraper import scrape_all_pages
from data_processor import save_to_csv

quotes_data = scrape_all_pages()

if quotes_data:
    save_to_csv(quotes_data)
else:
    print("No data scraped")