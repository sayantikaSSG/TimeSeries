import yfinance as yf
import pandas as pd
import os

# ----------- PARAMETERS -----------
TICKERS = ["^GSPC"]  # S&P 500
START_DATE = "2010-01-01"
END_DATE = "2025-11-25"
DATA_PATH = "../data/raw"  # relative path to save raw data
# ---------------------------------

# Ensure folder exists
os.makedirs(DATA_PATH, exist_ok=True)

def fetch_and_save_data(tickers, start, end, data_path):
    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        df = yf.download(ticker, start=start, end=end)
        # Save to CSV
        filename = os.path.join(data_path, f"{ticker.replace('^','')}_raw.csv")
        df.to_csv(filename)
        print(f"Saved {filename}")

if __name__ == "__main__":
    fetch_and_save_data(TICKERS, START_DATE, END_DATE, DATA_PATH)
