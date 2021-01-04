#Jake Roux
#I pledge my honor that I have abided by the Stevens honor system
import yfinance as yf
import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import datetime as dt
from datetime import date

print("The program will take three stock tickers and compare their cumulative returns")
print("from a date you select to present day")

tick1 = input("Enter Stock Ticker #1:")
tick2 = input("Enter Stock Ticker #2:")
tick3 = input("Enter Stock Ticker #3:")

list = [tick1, tick2, tick3]

date = input("Enter The Date You Want To See Data From (YYYY-MM-DD):")

price_data = yf.download(list,date)['Adj Close']

print(price_data)

graph = ((price_data.pct_change()+1).cumprod()).plot(figsize=(15,8))

plt.legend()
plt.title('Cumulative Returns Based On Date', fontsize=20)
plt.ylabel('Cumulative Returns', fontsize=15)
plt.xlabel('Date', fontsize=15)
plt.grid(color='k',linestyle='solid', linewidth=0.5)
plt.show()