import yfinance as yf
import matplotlib.pyplot as plt

def main():
    stock_input = input("Enter a ticker of a stock with a PE and Dividend Yield you would like a recommendation for: ")
    stock = yf.Ticker(stock_input)
    
    trailing_PE = stock.info["trailingPE"]
    print("The PE of", stock_input, "is:", trailing_PE)
    div_yield = stock.info["dividendYield"] * 100
    print("The Dividend Yield of", stock_input, "is:", div_yield, "%")
    
    if trailing_PE < 30 and 3 < div_yield < 6:
        print("I fully recommend buying this stock based on both PE and Dividend Yield.")
    elif trailing_PE < 30 and (3 > div_yield or 6 < div_yield):
        print("I recommend buying this stock based on PE but not Dividend Yield.")
    elif trailing_PE > 30 and 3 < div_yield < 6:
        print("I recommend buying this stock based on Dividend Yield but not PE.")
    else:
        print("I do not recommend buying this stock based on PE or Dividend Yield.")

    print()

    print("The graph of the price of your stock over the past year:")
    df = stock.history(period="1y")
    plt.plot(df.index, df["Close"], label="Close")
    plt.plot(df.index, df["Open"], label="Open")
    plt.plot(df.index, df["High"], label="High")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=90)
    plt.title("{}Stock Prices".format(stock_input.upper()))
    plt.legend(loc="upper left")
    plt.grid()
    plt.show()



main()
