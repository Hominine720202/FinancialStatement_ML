import pandas as pd
import os


def generate_filenames(path):
    return [name for name in sorted(os.listdir(path))]


def load_dataframe(filename, path, isCSV=True):
    if isCSV:
        return pd.read_csv(os.path.join(path, filename))
    else:
        return pd.read_json(os.path.join(path, filename))


def add_price_pct_change(dataframe, close0, close1):
    dataframe['Price % Change'] = ((close1['Adj Close'] - close0['Adj Close']) / close0['Adj Close']).transpose()
    return dataframe


# 1 Generate filenames
financials_files = generate_filenames(FINANCIALS_PATH)
close_files = generate_filenames(PRICE_PATH)

# 2 Generate DataFrames from the files
financials = [load_dataframe(f, FINANCIALS_PATH) for f in financials_files]
closes = [load_dataframe(c, PRICE_PATH) for c in close_files]

# 3 Generate list of the combined DataFrames - financials + price_percent_change
dfs = [add_price_pct_change(year, closes[index], closes[index+1]) for index, year in enumerate(financials)]