import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import pprint

pd.set_option('display.max_columns', None)
pretty = pprint.PrettyPrinter(indent=4)


def main():
    ticker = input("what Stock ticker would you like to analyze?(all caps)")#asks user for ticker
    print(ticker)

    timePeriod = input("Would you like to analyize since listing?(Type yes or no)")
    print(timePeriod)
    if timePeriod == "yes":
        tickerMax = yf.Ticker(ticker)
        tickerData = tickerMax.history(period="max")#retrieves the longest available set of data for that stock
        df = pd.DataFrame(tickerData) # turns downloaded data into a dataframe
        del df['Dividends']  # deleted excess data for processing speed and ram usage purposes
        del df['High']
        del df['Low']
        del df['Stock Splits']
        del df['Volume']
    elif timePeriod == "no":  # option if user wants to create their own time period
        specificStart = input("Please enter a start date in the format Year,Month,Day each sperated by '-'")
        specificEnd = input("Please enter an end date in the format Year,Month,Day each sperated by '-'")
        tickerData = yf.download(ticker, start=specificStart, end=specificEnd)  # downloads specific data using yfinance
        df = pd.DataFrame(tickerData)  # turns downloaded data into a dataframe
        del df['Adj Close']  # deleted excess data for processing speed and ram usage purposes
        del df['High']
        del df['Low']
        del df['Volume']
    else:
        print("False response, please rerun program") #response in case of bad input from user

    df["AH close"] = df["Open"].shift(periods=-1) #shifts 'open' down a row which creates the AH close
    df.drop(df['AH close'].tail(1).index, inplace=True) #deletes null row off the end of the new column

    df["AH open"] = df["Close"] #creates new column column AH open for simplification

    df['net g/l day'] = 0  # initializes net gains loss column
    df['%returns day'] = 0  # % returns column
    length = df.shape[0] #retrieves the length of the dataframe to find how many times to iterate the for loop

    initialpriceday = df['Open'].iloc[0] # sets the initial price to the first value of open
    
    currentpriceday = df['Open'].iloc[0] # initializes the current price by giving it the first open to start


    # for just the day
    for i in range(length - 1):
        daychange = (currentpriceday * ((df['Close'].iloc[i] - df['Open'].iloc[i]) / df['Open'].iloc[i]))#calculates thr ROI for the day
        totalmoneyday = daychange + currentpriceday #gives totalmoneyday a value and updates each iteration

        percentreturnsday = ((totalmoneyday - initialpriceday) / initialpriceday) * 100 #calculates thr ROI obtaining the % returns

        df['net g/l day'].iloc[i] = totalmoneyday # adds totalmoneyday to its iteration's row in df['net g/l day']

        df['%returns day'].iloc[i] = percentreturnsday # adds totalmoneyday to its iteration's row in df['net g/l day']

        currentpriceday = totalmoneyday #resets the current price to toal money to be reiterated

    df['net g/l night'] = 0 # initializes net gains loss column
    df['%returns night'] = 0# initializes % returns column

    initialpricenight = df['AH open'].iloc[0] # sets the initial price to the first value of AHopen

    currentpricenight = df['AH open'].iloc[0]  # initializes the current price by giving it the first AH open to start

    # for just the night
    for i in range(length):
        nightchange = (currentpricenight * ((df['AH close'].iloc[i] - df['AH open'].iloc[i]) / df['AH open'].iloc[i]))
        totalmoneynight = nightchange + currentpricenight

        percentreturnsnight = ((totalmoneynight - initialpricenight) / initialpricenight) * 100

        df['net g/l night'].iloc[i] = totalmoneynight

        df['%returns night'].iloc[i] = percentreturnsnight

        currentpricenight = totalmoneynight


    print()
    print("The net % of all normal market hours is: ", df['%returns day'].iloc[-2]) #presents final value of df['%returns day']
    print()
    print("The net % of all pre-market and after hours trading sessions is: ", df['%returns night'].iloc[-1]) #presents final value of df['%returns night']
    print()
    print("The last price of ",ticker,'is ', df['Close'].iloc[-1] )#presents the last price of chosen ticker

    print(df)
    df['%returns day'].plot(grid=True, label="Cumulative % of day") #plots Cumulative % of day
    df['%returns night'].plot(grid=True, label="Cumulative % of night") #plots Cumulative % of night
    plt.ylabel('Cumulative % returns')
    plt.title('Normal Trading Hours Vs. After Hours and Premarket Trading')
    plt.legend()
    plt.show()

main()