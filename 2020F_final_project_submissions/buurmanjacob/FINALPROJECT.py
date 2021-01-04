# Final Project
# By Jacob Buurman
# 12/13/2020
# I pledge my honor that I have abided by the Stevens Honor System.

# For this final project in CS110, I will be analyzing the charts of stocks that have been affected by
# the COVID-19 pandemic. The program will prompt the user to enter the ticker from a provided list of stocks,
# each of which I included in my CAL103 group research paper, where other QF/Finance majors and I delved into
# the sectors and industries who were impacted the most and how they adjusted to stay afloat. My job was to
# look at the companies and certain sectors that actually profited from the pandemic. The program will show
# the stock chart of the entered ticker and compare it to the chart of the respective index/indexes that company belongs
# to so that a visual representation of COVID's impact over the past year can be made.

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader as web

print("This program will allow the user to take a look at certain stocks that I did research on for my CAL103 research paper.\n\n"
      "These stocks profitted during the COVID-19 pandemic for various reasons, such as the increased reliance on tech in daily "
      "life,\n the race to develop a vaccine, or simply due to an increase in demand for certain items a company already produced.\n\n"
      "Take notice of general positive trends and/or speedy recoveries of these stocks through the beginning months of the pandemic\n (March, April) "
      "while the NASDAQ and S&P500 had large losses during that same period of time. \n\nHere is a list of stocks from the paper (in alphabetical "
      "order) that you can choose from to see how they profited in comparison\n to the index they belong to:\n\n"
      "(1) Activision Blizzard - ATVI | (2) Amazon - AMZN | (3) AstraZeneca - AZN | (4) BioNTech - BNTX | (5) Clorox - CLX | (6) eBay - EBAY |\n"
      "(7) Electronic Arts - EA | (8) Johnson & Johnson - JNJ | (9) Kroger - KR | (10) Moderna - MRNA | (11) Netflix - NFLX | (12) Nikola - NKLA |\n"
      "(13) PayPal - PYPL | (14) Peloton - PTON | (15) Pfizer - PFE | (16) Regeneron - REGN | (17) Weis Markets - WMK | (18) Zoom - ZM |\n")

def main():

    num = eval(input("Enter the number associated with the ticker of the stock you would like to see\n"
                     "(Note: you will need to X out of the first stock chart to see the next index chart(s)): "))

    style.use("ggplot")
    start = dt.datetime(2020,1,1)
    end = dt.datetime(2020,12,31)

    # Tickers
    if num == 1:
        df = web.get_data_yahoo("ATVI", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    elif num == 2:
        df = web.get_data_yahoo("AMZN", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    elif num == 3:
        df = web.get_data_yahoo("AZN", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    elif num == 4:
        df = web.get_data_yahoo("BNTX", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    elif num == 5:
        df = web.get_data_yahoo("CLX", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    elif num == 6:
        df = web.get_data_yahoo("EBAY", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    elif num == 7:
        df = web.get_data_yahoo("EA", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    elif num == 8:
        df = web.get_data_yahoo("JNJ", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    elif num == 9:
        df = web.get_data_yahoo("KR", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    elif num == 10:
        df = web.get_data_yahoo("MRNA", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    elif num == 11:
        df = web.get_data_yahoo("NFLX", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    elif num == 12:
        df = web.get_data_yahoo("NKLA", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    elif num == 13:
        df = web.get_data_yahoo("PYPL", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    elif num == 14:
        df = web.get_data_yahoo("PTON", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    elif num == 15:
        df = web.get_data_yahoo("PFE", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    elif num == 16:
        df = web.get_data_yahoo("REGN", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    elif num == 17:
        df = web.get_data_yahoo("WMK", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    elif num == 18:
        df = web.get_data_yahoo("ZM", start, end)
        df["Adj Close"].plot(color="red")
        plt.show()
    else:
        print("Error - enter a number from 1 to 18 associated with the list of stocks above.")

    # NASDAQ
    if num == 1 or num == 2 or num == 3 or num == 4 or num == 6 or num == 7 or num == 10 or num == 11 or num == 12 or num == 13 or num == 14 or num == 16 or num == 18:
        print(num, "is red, NASDAQ is blue.")
        df2 = web.get_data_yahoo("^IXIC", start, end)
        df2["Adj Close"].plot(color="blue")
        plt.show()
        print("This stock is listed on the NASDAQ Composite Index.")
    else:
        print("This stock is not listed on the NASDAQ Composite Index.")

    # S&P500
    if num == 1 or num == 2 or num == 5 or num == 6 or num == 7 or num == 8 or num == 9 or num == 11 or num == 13 or num == 15 or num == 16:
        print(num, "is red, S&P500 is green.")
        df2 = web.get_data_yahoo("^GSPC", start, end)
        df2["Adj Close"].plot(color="green")
        plt.show()
        print("This stock is listed on the S&P500 Index.")
    else:
        print("This stock is not listed on the S&P500 Index.")

    # Both
    if num == 1 or num == 2 or num == 6 or num == 7 or num == 11 or num == 13 or num == 16:
        print("This stock is listed on both the NASDAQ and S&P500 Indexes.")

    # Neither
    if num == 17:
        print("This stock (Weis Markets - WMK) is not listed on either index.")

main()

