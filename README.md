# Financial Statement Analysis - Machine-Learning
Analyse company Cash-Flow, Income Statement & Balance Sheet to predict if a stock's performance will beat the market.

### Datasets
- /datasets/financials directory contains the raw webscraped data from Yahoo Finance for each stock.
- /datasets/closes directory contains the close data for each stock pulled from the pandas_datareader API.
- /datasets/sp500_pct_change_list.csv contains the % associated % change of the S&P500 year on year, starting from 2015-2016, ending with 2018-2019.
- /datasets/features_labels directory contains DataFrame information with the features generated from the feature engineering (see generate_features.py) of the raw financial statement data, as well as associated labels (does this stock beat the S&P500?).
