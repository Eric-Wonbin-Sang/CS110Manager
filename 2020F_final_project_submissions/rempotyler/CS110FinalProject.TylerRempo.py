#I pledge my honor I have abided by the Stevens Honor Code
#How have select index funds and the value of gold, silver, and crude oil performed this year compared to the tech sector
#This program compares the cumulative returns of the index funds and gold, silver, and crude oil, in comparison to
#BlackRock's Tech Sector ETF for the whole year
#The index funds are the S&P 500, Dow Jones, Nasdaq, Russel 2000, SPDR S&P 500
#The commodities are Gold, Silver and Crude Oil
#The tech sector ETF is iShares Expanded Tech Sector ETF

import numpy as np
#For proccessing a large amount of mathematical functions
import pandas as pd
#For data analysis
from pandas_datareader import data as wb
#To get data from Yahoo Finance (DataSource)
import matplotlib.pyplot as plt
#For graphing data
def main():
    print("This program will provide you with a graph of the cumulative returns of select index funds in the US")
    print("and the cumulative returns of the value of Gold, Silver, and Crude Oil compared to the cumulative")
    print("returns of a Tech Sector ETF, IGM, over the past year.")
    UserInput = input("Enter 1 if you would like to view this graph: ")
    if UserInput in ["1.0", "1"]:
        # Array of stock objects
        stocks = [
            {
                'StockTicker': 'IGM',
                'StockName': 'iShares Expanded Tech Sector ETF'
            },
            {
                'StockTicker': '^GSPC',
                'StockName': 'S&P 500'
            },
            {
                'StockTicker': '^DJI',
                'StockName': 'Dow Jones Industrial Average'
            },
            {
                'StockTicker': '^IXIC',
                'StockName': 'NASDAQ Composite'
            },
            {
                'StockTicker': '^RUT',
                'StockName': 'Russel 2000'
            },
            {
                'StockTicker': 'SPY',
                'StockName': 'SPDR S&P 500 ETF Trust'
            },
            {
                'StockTicker': 'GC=F',
                'StockName': 'Gold'
            },
            {
                'StockTicker': 'SI=F',
                'StockName': 'Silver'
            },
            {
                'StockTicker': 'CL=F',
                'StockName': 'Crude Oil'
            }
        ]
        def create_plot(stocks):
            # Creating a dataframe
            data = pd.DataFrame()
            for stock in stocks:
                # Creating a column for the adjusted close of each stock
                # Using DataReader library to get data
                data[stock['StockTicker']] = wb.DataReader(stock['StockTicker'], data_source='yahoo', start='2020-1-1')[
                    'Adj Close']
                # Now have dates associated with adjusted closing price for each stock
                # Calculating returns for each day
                # Use lambda to create a function for calculating returns
            returns = data.apply(lambda x: (x / x[0] * 100))
            plt.figure(figsize=(10, 6))
            # Plotting returns
            for stock in stocks:
                plt.plot(returns[stock['StockTicker']], label=stock['StockName'])
                # Use .legend() to show graph 'legend'
            plt.legend()
            # Label the axes
            plt.ylabel('Cumulative Return Percentage')
            plt.xlabel('Time')
            plt.show()
        create_plot(stocks)
        #If anything else is typed other than 1, whether numerical or string it will print this
    else:
        print("Welp I guess you aren't interested in the graph.")
main()