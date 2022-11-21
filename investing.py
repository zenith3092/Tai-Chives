import pandas as pd


class InvestTool:
    def __init__(self, symbol):
        self.method = ""


class Stock:
    def __init__(self, symbol, path):
        self.symbol = symbol
        self.path = path
        self.data = self.get_data()
        self.adj_close = pd.to_numeric(self.data['Adj Close'])
    
    def get_data(self):
        df = pd.read_csv(self.path)
        df = df.set_index(pd.to_datetime(df['Date'], format = "%Y/%m/%d"))
        df = df.drop('Date', axis = 1)
        return df


if __name__ == "__main__":
    TW2330 = Stock("2330", "/Users/zenith3092/Documents/Tai-Chives/data/2330_TW.csv")
    print(TW2330.symbol)
    print(TW2330.path)
    print(TW2330.data)
    print(TW2330.adj_close)

    TW2404 = Stock("2404", "/Users/zenith3092/Documents/Tai-Chives/data/2404.TW.csv")
    print(TW2404.symbol)
    print(TW2404.adj_close)
