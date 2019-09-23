import datetime as dt
import time
from pandas_datareader import data
import pandas as pd
from io import StringIO
import numpy as np


# Handles incomplete years
def get_stock_close_avg(tickers, year):
    avg_closes = pd.DataFrame()

    # Generate current year (str --> int)
    current = dt.datetime.now().strftime('%Y-%m-%d')
    c_year = int(current[0:4])

    # If given argument 'year' is the current year (ie. incomplete) modify start&end dates accordingly
    if year == c_year:
        month = int(current[5:7])
        start = dt.datetime(year, month - 1, 1)
        end = dt.datetime.now()

    # Else (historically complete year, proceed as normal)
    else:
        month = 12
        day_start = 1
        day_end = 31
        start = dt.datetime(year, month, day_start)
        end = dt.datetime(year + 1, month - 11, day_end)

    # Iterate through all tickers to fill avg_closes DataFrame with each stock as a row
    for index, ticker in enumerate(tickers):
        time.sleep(1)
        try:
            df = data.DataReader(ticker, 'yahoo', start, end)
            close_avg = pd.Series(df['Adj Close'].mean())
            avg_closes = pd.concat([avg_closes, close_avg], axis=0)
        except:
            print(f'No data found (added NaN in row) for tickers[{index}]: {ticker}')
            close_avg = pd.Series(np.nan)
            avg_closes = pd.concat([avg_closes, close_avg])

    avg_closes.index = tickers
    avg_closes.columns = ['Adj Close']

    return avg_closes