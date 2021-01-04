import math
import yfinance as yf
import matplotlib.pyplot as plt

class Index:

    def __init__(self, index_ticker, date1, date2):

        #variables
        self.index_ticker = index_ticker
        self.start_date = date1
        self.end_date = date2

        self.ticker_data = yf.Ticker(index_ticker)

        #get the historical prices for this ticker
        self.ticker_prices = self.ticker_data.history(period='1d', start=date1, end=date2)

        self.ticker1 = self.ticker()

        #returns the ticker
    def ticker(self):
        return self.ticker_prices
#this function makes sure the date that is entered is valid 

def date(date):
    
    year,month,day = date.split('-')
    month = int(month)
    day = int(day)
    year= int(year)

    
    if year > 2020:
        return "Your date is invalid, sorry."
    elif month > 12:
        return "Your date is invaild, sorry."
    elif (month == 1 or month == 3  or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        if day > 31:
            return "Your date is invalid, sorry."
        else:
            return "Your date is valid"
    elif month == 2 and day > 29:
        return "Your date is invalid, sorry."
    elif (month == 4 or month == 6 or month == 9 or month == 11):
        if day > 30:
            return "Your date is invalid, sorry,"
        else:
            return "Your date is valid"
    else:
        return "Your date is valid"
#this graph the stock's you've choosen in the time interval
def make_graph(data_frames,ticker_list):

    for i in range(len(data_frames)):
        plt.plot(data_frames[i]['Close'], label=ticker_list[i])
    
    plt.legend(loc="upper left")
    plt.xlabel("Date")
    plt.ylabel("Close Price")

    if(len(ticker_list) > 1):
        plt.title("Comparison of stocks")
    else:
        plt.title("Price Data for " + ticker_list[0].upper())

    plt.style.use('dark_background')
    plt.show()
    

def main():
    #Asking for how many tickers we need to go through
    list_length = int(input("How many stocks are in your portfolio: "))
    ticker_list = []
    #did a while loop so we can continue the function if the user enters a invalid ticker
    i = 0
    while i < list_length:

        ticker = input("Enter ticker name: ")
        #this try catch conditional makes sure that the ticker that is typed in is actually a valid stock
        try:
            yf.Ticker(ticker).info
        
        except ValueError:
            print(ticker, "does not exist, please enter a valid ticker")
            continue
        #once it goes through the try-catch, the ticker is added to the ticker list
        ticker_list.append(ticker)
        i = i + 1

    j = 0
    #this loop asks for the date from start to end
    while j < 1:
        start_date = input("Enter start date in form YEAR-MONTH-DAY: ")
        end_date = input("Enter end date in form YEAR-MONTH-DAY: ")
        #putting the inputs in our date checker function above
        check_date1 = date(start_date)
        check_date2 = date(end_date)
        #if the function returns this string it accepts the date, if not, it continues to loop until it recieves valid dates
        if check_date1 != "Your date is valid" and check_date2 != "Your date is valid":
            print("You've entered an invaild date, please enter a new date")
            continue

        else:
            print("Date is valid")
            j = j + 1
            
    #this part is calculating the percent change in the function over the interval of time
    frame_list = []
    percent_list = []
    for ticker in ticker_list:
        frame = Index(ticker, start_date, end_date).ticker_prices
        frame_list.append(frame)
        last_close = frame["Close"][-1]
        first_close = frame["Close"][0]
        percent_increase = (last_close - first_close)/first_close * 100
        print("Here's the first close for the start date:", round(first_close,2))
        print("Here's the last close for the end date:", round(last_close,2))
        print("This is the percentage change for" , ticker.upper(), "in the period you listed:",  str(round(percent_increase,2)), "%")
        #add the percent change to the list
        percent_list.append(percent_increase)
    #need to find the best performing stock based on percentage change
    best_performer_index = percent_list.index(max(percent_list))
    best_performer = max(percent_list)
    print("The best performer of the stocks you selected was", ticker_list[best_performer_index],"with a ", str(round(best_performer,2)),"% ")
    #Using the function to graph all the tickers
    make_graph(frame_list,ticker_list)
    
main()
