import yfinance as yf
import pandas as pd
import numpy as np
import pandas_datareader as web
import matplotlib.pyplot as plt
from datetime import date
import datetime as dt
#This code can help one see how their stocks have performed compared to the market index. (SPY)
ans1 = input("Enter your Ticker symbol:")
ans2 = input("Enter your Ticker symbol:")
ans3 =input("Enter your Ticker symbol:")
tickers_list = ['spy', ans1, ans2, ans3]
date= input("Enter the date you would like to start from(YYYY-MM-DD Format):")
data = yf.download(tickers_list,date)['Adj Close']
print(data.head())
final = ((data.pct_change()+1).cumprod()).plot(figsize=(10, 7))
plt.legend()

plt.title("Returns", fontsize=11)
plt.ylabel('Cumulative Returns', fontsize=18)
plt.xlabel('Year-month', fontsize=10)
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.4)
plt.show()

