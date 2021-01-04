import yfinance as yf
import matplotlib.pyplot as plt

def main():

    print("Welcome to your personal Investment Advisory Program!")
    print("Directions are as follows: ")
    print("1.) Enter the tickers for the 2 stocks you would like to compare")
    print( "2.) The program will use the Price to Earnings ratio and the Dividend Yield to calculate which is the better investment")
    print("3.) The program will then graph the stock it chose with the S and P 500")
    print("4.) If this program is unable to indentify one stock due to these two metrics you will be notified. If this occurs both stocks will be graphed")
    print("Disclaimer: In order for this program to work it is important that you pick stocks which offer both a P/E value and a Dividend Yield")

    stock1 = input("Please enter the ticker of the first stock you have chosen: ")
    company1 = yf.Ticker(stock1)
    stock2 = input("Now enter the ticker of the second stock you would like to choose: ")
    company2 = yf.Ticker(stock2)
    print("The two tickers you would like to compare are", stock1, "and", stock2)
    sandp500 = yf.Ticker("^GSPC")

    divyld1 = company1.info["dividendRate"]
    divyld2 = company2.info["dividendRate"]
    pe1 = company1.info["trailingPE"]
    pe2 = company2.info["trailingPE"]

    if divyld1 > divyld2 and pe1 < pe2:
        print(stock1, "is the best investment if evaluated by the two metrics used")
        print("Here is the graph of the stock the program has identififed as the better investment graphed with the S and P 500")
        chart1 = company1.history(start="2020-01-01")
        plt.plot(chart1.index, chart1["Close"], label="Close")
        plt.plot(chart1.index, chart1["Open"], label="Open")

        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.title(stock1)
        plt.legend(loc="upper left")
        plt.grid()
        plt.show()

        sandp = sandp500.history(start="2020-01-01")
        plt.plot(sandp.index, sandp["Close"], label="Close")
        plt.plot(sandp.index, sandp["Open"], label="Open")

        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.title("The S and P 500")
        plt.legend(loc="upper left")
        plt.grid()
        plt.show()

    elif divyld1 < divyld2 and pe1 > pe2:
        print(stock2, "is the best investment if evaluated by the two metrics used")
        print("Here is the graph of the stoc the program has dentififed as the better investment graphed with the S and P 500")
        chart2 = company2.history(start="2020-01-01")
        plt.plot(chart2.index, chart2["Close"], label="Close")
        plt.plot(chart2.index, chart2["Open"], label="Open")

        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.title(stock2)
        plt.legend(loc="upper left")
        plt.grid()
        plt.show()

        sandp = sandp500.history(start="2020-01-01")
        plt.plot(sandp.index, sandp["Close"], label="Close")
        plt.plot(sandp.index, sandp["Open"], label="Open")

        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.title("The S and P 500")
        plt.legend(loc="upper left")
        plt.grid()
        plt.show()

    else:
        print("We cannot formulate the best investment while using these two metrics")
        print("Here is the graph of both the stocks you entered and the S and P 500 to assist you on how each company is doing compared to the market.")
        chart1 = company1.history(start="2020-01-01")
        plt.plot(chart1.index, chart1["Close"], label="Close")
        plt.plot(chart1.index, chart1["Open"], label="Open")

        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.title(stock1)
        plt.legend(loc="upper left")
        plt.grid()
        plt.show()

        chart2 = company2.history(start="2020-01-01")
        plt.plot(chart2.index, chart2["Close"], label="Close")
        plt.plot(chart2.index, chart2["Open"], label="Open")

        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.title(stock2)
        plt.legend(loc="upper left")
        plt.grid()
        plt.show()

        sandp = sandp500.history(start="2020-01-01")
        plt.plot(sandp.index, sandp["Close"], label="Close")
        plt.plot(sandp.index, sandp["Open"], label="Open")

        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.title("The S and P 500")
        plt.legend(loc="upper left")
        plt.grid()
        plt.show()

    print("Thank you for using our advisory program!")

main()
