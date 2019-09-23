from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import numpy as np

def generate_mc_urls(tickers):
    mc_urls = []
    for ticker in tickers:
        url = f"https://finance.yahoo.com/quote/{ticker}?p={ticker}"
        mc_urls.append(url)
    return mc_urls


def marketcap_scrape(mc_urls):
    mcs = []
    for index, url in enumerate(mc_urls):
        try:
            source = requests.get(url).text
            soup = BeautifulSoup(source, 'lxml')
            table = soup.find('table', class_='W(100%) M(0) Bdcl(c)')
            mc = table.tr.find('span', class_='Trsdu(0.3s)').text
            mcs.append(mc)
            time.sleep(1)
        except:
            print("Ticker number ", index, "did not scrape = no value?")
            mcs.append(np.nan)

    return pd.DataFrame(data=[mcs], columns=['Market Cap 2019'])