import csv
import math
import pickle
import graphics
import yfinance as yf
import pprint
import pandas as pd


pd.set_option('display.max_columns', None)

pretty = pprint.PrettyPrinter(indent = 4)

def main():

    # Downloading the history of 3 stocks i am using (Vanguards S&P 500, mid-cap, small-cap prices)
    # Using yfinance rather than importing csv file
    ticker_list = []
    print("Enter three different stock tickers to see which stock has the highest percent change since the first announcement of covid.")
    for i in range(3):
        data = str(input())
        ticker_list.append(data)

    index_list = [yf.Ticker(ticker) for ticker in ticker_list]

    # get each history in own dataframe
    df3 = index_list.pop().history(start = "2020-01-21")
    df2 = index_list.pop().history(start = "2020-01-21")
    df1 = index_list.pop().history(start = "2020-01-21")

    print(df1)
    print(df2)
    print(df3)
    #If i was only using VOO, VO, VB and no list
    # VOO_df = yf.Ticker('VOO').history(start = "2020-01-21")
    # VO_df = yf.Ticker('VO').history(start = "2020-01-21")
    # VB_df = yf.Ticker('Vb').history(start = "2020-01-21")
    # print(VOO_df)
    # print(VO_df)
    # print(VB_df)
    # print(VOO_df.describe())
    # print(VO_df.describe())
    # print(VB_df.describe())

    # Get the closing price of day pandemic started to the last imputed closing price
    ticker1past = df1['Close'].iloc[0]
    ticker1present = df1['Close'].iloc[-1]
    ticker2past = df2['Close'].iloc[0]
    ticker2present = df2['Close'].iloc[-1]
    ticker3past = df3['Close'].iloc[0]
    ticker3present = df3['Close'].iloc[-1]

    # get each percent change for each ticker
    ticker1increase = ticker1present - ticker1past
    ticker1percentchange = (ticker1increase/ticker1past)*100
    ticker2increase = ticker2present - ticker2past
    ticker2percentchange = (ticker2increase/ticker2past)*100
    ticker3increase = ticker3present - ticker3past
    ticker3percentchange = (ticker3increase / ticker3past) * 100

    # Using dictionary rather than class because if is faster for my purpose
    Stock3 = ticker_list.pop()
    Stock2 = ticker_list.pop()
    Stock1 = ticker_list.pop()
    thisdict = {
        ticker1percentchange : Stock1,
        ticker2percentchange : Stock2,
        ticker3percentchange : Stock3
    }
    #Test which stock has highest percent change
    highestpercentchange = -100
    percentchange_list = [ticker1percentchange, ticker2percentchange, ticker3percentchange]

    for i in percentchange_list:

        if i > highestpercentchange:
            highestpercentchange = i


    print((thisdict[highestpercentchange]) + " has done the best since the first case of coronavirus was announced in the US with a percent change of " + str(highestpercentchange) + "%")

main()

