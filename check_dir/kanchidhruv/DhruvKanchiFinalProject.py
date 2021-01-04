# I pledge that I have abided by the Stevens Honor System. 


import pprint
import yfinance as yf
import pandas
import matplotlib.pyplot as plt

pp = pprint.PrettyPrinter(indent=5)
pandas.set_option('display.max_columns', None)



def getTickerInput():
    return str(input("Please enter the ticker of your stock(Make sure it has a reported PE ratio or divdend yield): "))


def getStock(anyTicker):
    return yf.Ticker(anyTicker)


def getStockDividendRate(anyStock):
    return (anyStock.info["dividendYield"])*100

def getPERatio(anyStock):
    return anyStock.info["trailingPE"]

def graphStock(anyStock, anyTicker):

    df = anyStock.history(period="ytd")

    plt.plot(df.index, df["Close"], label="Close")
    plt.plot(df.index, df["Open"], label="Open")

    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=90)
    plt.title("{} Stock Prices".format(anyTicker.upper()))
    plt.legend(loc="upper left")
    plt.grid()

    plt.show()


def main():

    while True:
        ticker = getTickerInput()
        print(ticker)

        stock = getStock(ticker)
        print(stock)

        print("the dividend yield of your stock is", getStockDividendRate(stock),"%")

        print("the PE ratio of your stock is", getPERatio(stock))

        print("a graph of your stock's closing and opening price over the calendar year will now appear")
        graphStock(stock, ticker)

        if getStockDividendRate(stock) >= 3 and getPERatio(stock) <= 25:
            print("This is a solid investment, and I recommend making it based on the stock's PE ratio and dividend yield.")
        elif getStockDividendRate(stock) < 3 and getPERatio(stock) <= 25:
            print("This is a potentially good investment, I recommend making it based on the stock's PE ratio.")
        elif getStockDividendRate(stock) >= 3 and getPERatio(stock) > 25:
            print("This is a potentially good investment, I recommend making it based on the stock's dividend yield.")
        else:
            print("Look for better oppurtunities, this stock isn't the best option right now")

main()
