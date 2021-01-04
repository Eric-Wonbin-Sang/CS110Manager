
import yfinance as yf
import plotly.express as px
# I pledge my honor that I have abided by the Stevens Honor Code.
#Riley Sikorski

def main():
    #This program will answer the following question using a graph:
    #How do the closing prices of two stocks over the last 10 months, as affected by the pandemic, compare?
    #The user will choose which two stocks (from 4 options) they wish to compare.



    print("You can choose which 2 stocks from the list of 4 that you would like to compare.")
    print("1 = Apple (AAPL)")
    print("2 = Microsoft (MSFT)")
    print("3 = Facebook (FB)")
    print("4 = Amazon (AMZN)")
    first = eval(input("Please enter the number for the first stock you would like to compare: "))
    second = eval(input("Please enter the number for the second stock you would like to compare (please do not repeat): "))
    if first == 1:
        apple = yf.Ticker('AAPL')
        data1 = apple.history(start="2020-03-01", end= "2020-12-01")
        data1 = data1.reset_index()
        graph1 = px.line(data1, x="Date", y="Close", title='Apple Closing Prices')
        graph1.show()
        print("You are comparing the closing prices of Apple ")
    elif first == 2:
        microsoft = yf.Ticker('MSFT')
        data1 = microsoft.history(start="2020-03-01", end="2020-12-01")
        data1 = data1.reset_index()
        graph1 = px.line(data1, x="Date", y="Close", title='Microsoft Closing Prices')
        graph1.show()
        print("You are comparing the closing prices of Microsoft ")
    elif first == 3:
        facebook = yf.Ticker('FB')
        data1 = facebook.history(start="2020-03-01", end= "2020-12-01")
        data1 = data1.reset_index()
        graph1 = px.line(data1, x="Date", y="Close", title='Facebook Closing Prices')
        graph1.show()
        print("You are comparing the closing prices of Facebook ")
    elif first == 4:
        amazon = yf.Ticker('AMZN')
        data1 = amazon.history(start="2020-03-01", end= "2020-12-01")
        data1 = data1.reset_index()
        graph1 = px.line(data1, x="Date", y="Close", title='Amazon Closing Prices')
        graph1.show()
        print("You are comparing the closing prices of Amazon ")

    if second == 1:
        apple = yf.Ticker('AAPL')
        data2 = apple.history(start="2020-03-01", end= "2020-12-01")
        data2 = data2.reset_index()
        graph2 = px.line(data2, x="Date", y="Close", title='Apple Closing Prices')
        graph2.show()
        print(" to the closing prices of Apple.")
    elif second == 2:
        microsoft = yf.Ticker('MSFT')
        data2 = microsoft.history(start="2020-03-01", end= "2020-12-01")
        data2 = data2.reset_index()
        graph2 = px.line(data2, x="Date", y="Close", title='Microsoft Closing Prices')
        graph2.show()
        print(" to the closing prices of Microsoft.")
    elif second == 3:
        facebook = yf.Ticker('FB')
        data2 = facebook.history(start="2020-03-01", end= "2020-12-01")
        data2 = data2.reset_index()
        graph2 = px.line(data2, x="Date", y="Close", title='Facebook Closing Prices')
        graph2.show()
        print(" to the closing prices of Facebook.")
    elif second == 4:
        amazon = yf.Ticker('AMZN')
        data2 = amazon.history(start="2020-03-01", end= "2020-12-01")
        data2 = data2.reset_index()
        graph2 = px.line(data2, x="Date", y="Close", title='Amazon Closing Prices')
        graph2.show()
        print(" to the closing prices of Amazon.")


main()
