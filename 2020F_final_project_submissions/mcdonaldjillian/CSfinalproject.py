import yfinance as yf
from  matplotlib import pyplot as plt


def load_ticker(symbol):

    ticker  = yf.Ticker(symbol)
    hist = ticker.history(start="2020-03-01", end="2020-12-02")
    hist = hist.reset_index()
    for i in ['Open', 'High', 'Close', 'Low']:
        hist[i] = hist[i].astype('float64')

    return hist

def main():

    while True:

        print("Please choose one of the following choices: ")
        print("1. Display graph for NVDA and INTC")
        print("2. Display graph for INTC and AMD")
        print("3. Display graph for AMD and NVDA")
        print("4. Exit.")
        resp = input(">>> ")


        if resp == "1":
            h1 = load_ticker("NVDA")
            h2 = load_ticker("INTC")
            ax = h1[['Open']].plot(title="NVDA vs INTC")
            h2[['Open']].plot(ax=ax)
            plt.legend(["Open NVDA", "Open INTC"])
        if resp == "2":
            h1 = load_ticker("INTC")
            h2 = load_ticker("AMD")
            ax = h1[['Open']].plot(title="INTC vs AMD")
            h2[['Open']].plot(ax=ax)
            plt.legend(["Open INTC", "Open AMD"])
        if resp == "3":
            h1 = load_ticker("AMD")
            h2 = load_ticker("NVDA")
            ax = h1[['Open']].plot(title="AMD vs NVDA")
            h2[['Open']].plot(ax=ax)
            plt.legend(["Open AMD", "Open NVDA"])
        if resp == "4":
            break


        plt.show()


main()

