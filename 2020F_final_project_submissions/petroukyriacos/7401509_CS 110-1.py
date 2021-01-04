import pandas as pd
import yfinance as yf

import matplotlib.pyplot as plt


def CumulativeReturn1(tickers_list1):
    data = yf.download(tickers_list1, '2010-12-10', '2020-12-10')['Adj Close']
    data2 = yf.download(tickers_list1, '2010-12-10', '2020-12-10')['Open']
    # cumulative return calculation
    cum_return1 = (data - data2) / data * 100
    print(cum_return1)
    print(type(cum_return1))
    return cum_return1


def ticker_list1(cum_return, tickers_list1):
    x_axiss = []
    a = 0
    for i in tickers_list1:
        a = list(cum_return[i])
        x_axiss.append(a)
        print(len(x_axiss))
    return x_axiss


#  [[1],[2].......]

def main():
    tickers_list1 = ['AAPL', 'AMZN', 'MFST', '^GSPC', 'VGT', 'XLK', 'IYW']
    cum_return1 = CumulativeReturn1(tickers_list1)
    x_axiss1 = ticker_list1(cum_return1, tickers_list1)
    Year = pd.read_csv('AAPL.csv')
    year = list(Year["Date"])
    for i in range(len(x_axiss1)):
        plt.plot(year, x_axiss1[i], label=tickers_list1[i])
    plt.legend()
    plt.title("Returns", fontsize=16)
    plt.ylabel("Cumulative Returns", fontsize=14)
    plt.ylim(-100, 100)
    plt.xlabel('Year', fontsize=14)
    plt.xticks(rotation=90)
    plt.grid()
    plt.show()


main()

# ((data.pct_change()+1).cumprod()).plot(figsize=(10, 7))


# plot Cumulative Returns
#
