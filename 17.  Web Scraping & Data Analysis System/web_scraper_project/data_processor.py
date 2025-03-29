import pandas as pd

def save_to_csv(data, filename="output/scraped_quotes.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
    