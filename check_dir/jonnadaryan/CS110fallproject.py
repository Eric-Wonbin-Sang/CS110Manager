#I pledge that I have abided by the Stevens Honor System

import yfinance as yf

import matplotlib.pyplot as plt

import time


class Stock():

    print("This program will present 5 stocks in the tech sector that performed well during the pandemic")
    ans = (input("Are you ready to continue?"))
    while ans != "yes":
        ans = input("The input is invalid, please type 'yes' to continue")
    print("5 stocks in the tech sector that performed well during the pandemic are"
          " Apple, Microsoft, Cloudflare, Adobe, and Nvidia")

    def plot_stock(self,company,start,end,name):

        data = yf.download(company,start,end)
        plt.style.use('dark_background')
        data['Adj Close'].plot()
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.title(name)
        plt.show()


tickers = ["SPY", "AAPL", "MSFT", "NVDA", "NET", "ADBE"]
start = "2020-01-01"
end = "2020-12-01"

print("")
print("Charts of these stock prices will appear in a pop up window within 10 seconds")
print("")
print("Once you are done viewing one chart, close the pop up window to view the next one")
print("")
print("While viewing graph, return to console to view information about the specific stock")

time.sleep(10)

stock = Stock()
stock.plot_stock("SPY", start, end, "SPY Stock Prices")
print("This is the S&P 500 which we will use as benchmark for these stocks to be compared to.")

stock.plot_stock("AAPL", start, end, "AAPL Stock Prices")
print("Although Apple had a decline in iphone sales form last year.  "
      "Due to the pandemic, their sales from laptops and iPads increased significantly ")

stock.plot_stock("MSFT", start, end, "MSFT Stock Prices")
print("Microsoft has seen a 12% increase in revenue and a 30% increase in net income "
      "due to how many people are working from home.")

stock.plot_stock("NVDA", start, end, "NVDA Stock Prices")
print("During the pandemic, the popularity in gaming increased.  "
      "However, Nvidia offers many gaming products which helped their recovery during the pandemic.")

stock.plot_stock("NET", start, end, "NET Stock Prices")
print("Due to the rise in hacking during the pandemic, "
      "there has been an increase in the need for Cloudflare's services which helped them weather the pandemic")

stock.plot_stock("ADBE", start, end, "ADBE Stock Prices")
print("Adobe sells services that help those who work remotely, "
      "and the pandemic has only increased their target audience")

stock.plot_stock(" ".join(tickers), start, end, "Comparison to S&P 500")
print("")
print("")
print("Thank you for viewing this code, I hope this helped!")









