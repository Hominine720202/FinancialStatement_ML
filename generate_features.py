import pandas as pd


PRICE_PATH = '/home/keir/it/1_DS/projects/FinancialStatement_ML/datasets/closes'
FINANCIALS_PATH = '/home/keir/it/1_DS/projects/FinancialStatement_ML/datasets/financials'


class CashFlow:
    # Automatically initialise Cash-Flow DataFrame
    def __init__(self, df):
        self.df = df
        self.tickers = df['index']
        self.cfdf = pd.DataFrame(self.tickers)
        # Apply class functions to Cash-Flow cfdf DataFrame
        self.cfdf = self.cf_311(self.df, self.cfdf)
        self.cfdf = self.cf_312(self.df, self.cfdf)
        self.cfdf = self.cf_313(self.df, self.cfdf)
        self.cfdf = self.cf_314(self.df, self.cfdf)
        self.cfdf = self.cf_315(self.df, self.cfdf)
        self.cfdf = self.cf_316(self.df, self.cfdf)

    # 3.1.1 Net Income Per Total Cash Flow From Operating Activities
    def cf_311(self, df, cfdf):
        self.cfdf['Net Income / Total CF OA'] = self.df['Net Income'] / self.df[
            'Total Cash Flow From Operating Activities']
        return cfdf

        # 3.1.2 True If Total Cash Flow From Operating Activites Is Positive

    def cf_312(self, df, cfdf):
        boolvals = []
        for row in self.df['Total Cash Flow From Operating Activities']:
            if row > 0:
                boolvals.append(True)
            else:
                boolvals.append(False)
        self.cfdf['Positive Total CF OA'] = boolvals
        return cfdf

    # 3.1.3 True If Net Income < Total Cash Flow From Operating Activities
    def cf_313(self, df, cfdf):
        boolvals = []
        for netincome, cf in zip(self.df['Net Income'], self.df['Total Cash Flow From Operating Activities']):
            if netincome < cf:
                boolvals.append(True)
            else:
                boolvals.append(False)

        self.cfdf['Net Income < Total CF OA'] = boolvals
        return cfdf

    # 3.1.4 True If Total Cash Flow From Operating Activities > Dividends Paid Out
    def cf_314(self, df, cfdf):
        boolvals = []
        for cf, dividends in zip(self.df['Total Cash Flow From Operating Activities'], self.df['Dividends Paid']):
            if cf > dividends:
                boolvals.append(True)
            else:
                boolvals.append(False)
        self.cfdf['Total CF OA > Dividends'] = boolvals
        return cfdf

    # 3.1.5 (-Net Borrowings) / Dividends Paid Out
    def cf_315(self, df, cfdf):
        self.cfdf['-Net Borrowings / Dividends'] = self.df['Net Borrowings'] / self.df['Dividends Paid']
        return cfdf

    # 3.1.6 Free Cash Flow / Total Cash Flow From Operating Activities
    def cf_316(self, df, cfdf):
        # Calculate Free Cash Flow ( = T CF OA + Capital Expenditure)
        self.df['fcf'] = self.df['Total Cash Flow From Operating Activities'] + self.df['Capital Expenditure']
        self.cfdf['FCF / Total CF OA'] = self.df['fcf'] / self.df['Total Cash Flow From Operating Activities']
        return cfdf


class IncomeStatement:
    # Automatically initialise Income Statement DataFrame
    def __init__(self, df):
        self.df = df
        self.tickers = df['index']
        self.isdf = pd.DataFrame(self.tickers)
        # Apply class functions to Income Statement isdf DataFrame
        # self.isdf = self.is_321(self.df, self.isdf)
        self.isdf = self.is_322(self.df, self.isdf)
        self.isdf = self.is_323(self.df, self.isdf)
        self.isdf = self.is_324(self.df, self.isdf)
        self.isdf = self.is_325(self.df, self.isdf)
        self.isdf = self.is_326(self.df, self.isdf)
        self.isdf = self.is_327(self.df, self.isdf)
        self.isdf = self.is_328(self.df, self.isdf)
        # self.isdf = self.is_329(self.df, self.isdf)

    # 3.2.1 Gross Profit / Market Cap
    # def is_321(self, df, isdf):
    #    pass

    # 3.2.2 Gross Profit / Total Revenue
    def is_322(self, df, isdf):
        self.isdf['R&D / Total OE'] = self.df['Research Development'] / self.df['Total Operating Expenses']
        return isdf

    # 3.2.3 Research&Development / Total Operating Expenses
    def is_323(self, df, isdf):
        self.isdf['R&D / Total OE'] = self.df['Research Development'] / self.df['Total Operating Expenses']
        return isdf

    # 3.2.4 Selling General & Admin / Total Operating Expenses
    def is_324(self, df, isdf):
        self.isdf['General&Admin OE / Total OE'] = self.df['Selling General and Administrative'] / self.df[
            'Total Operating Expenses']
        return isdf

    # 3.2.5 R&D / Gross Profit
    def is_325(self, df, isdf):
        self.isdf['R&D / Gross Profit'] = self.df['Research Development'] / self.df['Gross Profit']
        return isdf

    # 3.2.6 Operating Income Or Loss / Total Operating Expenses
    def is_326(self, df, isdf):
        self.isdf['Operating Income / Total OE'] = self.df['Operating Income or Loss'] / self.df[
            'Total Operating Expenses']
        return isdf

    # 3.2.7 Net Income From Continuing Ops / Gross Profit
    def is_327(self, df, isdf):
        self.isdf['Net Income From Continuing Ops / Gross Profit'] = self.df['Net Income From Continuing Ops'] / \
                                                                     self.df['Gross Profit']
        return isdf

    # 3.2.8 Net Income / Gross Profit
    def is_328(self, df, isdf):
        self.isdf['Net Income / Gross Profit'] = self.df['Net Income'] / self.df['Gross Profit']
        return isdf

    # 3.2.9 Net Income / Market Cap
    # def is_329(self, df, isdf):
    #    pass


class BalanceSheet:
    # Automatically initialise Balance Sheet DataFrame
    def __init__(self, df):
        self.df = df
        self.tickers = df['index']
        self.bsdf = pd.DataFrame(self.tickers)
        # Apply class functions to Balance Sheet bsdf DataFrame
        self.bsdf = self.bs_331(self.df, self.bsdf)
        # self.bsdf = self.s_332(self.df, self.bsdf)
        self.bsdf = self.bs_333(self.df, self.bsdf)
        self.bsdf = self.bs_334(self.df, self.bsdf)
        # self.bsdf = self.bs_335(self.df, self.bsdf)

    # 3.3.1 Net Tangible Assets / Total Assets
    def bs_331(self, df, bsdf):
        self.bsdf['Net Tangible Assets / Total Assets'] = self.df['Net Tangible Assets'] / self.df['Total Assets']
        return bsdf

    # 3.3.2 Net Tangible Assets / Market Cap
    # def is_332(self, df, bsdf):
    #    pass

    # 3.3.3 True Working Capital / Total Current Assets
    # '--> True working capital = Total Current Assets - Total Current Liabilities
    def bs_333(self, df, bsdf):
        self.df['True Working Capital'] = self.df['Total Current Assets'] - self.df['Total Current Liabilities']
        self.bsdf['True Working Capital / Total Current Assets'] = self.df['True Working Capital'] / self.df[
            'Total Current Assets']
        return bsdf

    # 3.3.4 True If True Working Capital Is Positive
    def bs_334(self, df, bsdf):
        self.df['True Working Capital'] = self.df['Total Current Assets'] - self.df['Total Current Liabilities']
        boolvals = []
        for row in self.df['True Working Capital']:
            if row > 0:
                boolvals.append(True)
            else:
                boolvals.append(False)
        self.bsdf['Positive True Working Capital'] = boolvals
        return bsdf

    # 3.3.5 Net Tangible Assets / Market Cap
    # def is_335(self, df, bsdf):
    #    pass