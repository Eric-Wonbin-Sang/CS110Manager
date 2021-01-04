import os
import csv
import matplotlib.pyplot as graph
from numpy import mean


def get_csv_files():
    csv_files = "C:/Users/nicle/PycharmProjects/week 13/csv"
    csv_file_list = []
    for file in os.listdir(csv_files):
        csv_file_list.append(csv_files + "/" + file)
    return csv_file_list

def get_ticker_from_file(file):
    CompanyName = file.split("csv/")[-1][:-4]
    return CompanyName

def get_date_and_price_list_from_csv(file_name):
    date_list, close_list = [], []
    with open(file_name) as csv_file:
        for row in list(csv.reader(csv_file))[1:]:
            date_list.append(row[0])
            close_list.append(float(row[4]))
        return date_list, close_list

def graph_xlist_and_ylist(x, y, CompanyName):
    graph.plot(x, y, label=CompanyName)

def show_graph():
    graph.xlabel("Date")
    graph.ylabel("Closing Price")
    graph.xticks(rotation=90)
    graph.title("Closing Prices of Tech Sector Stocks Throughout The Pandemic")
    graph.legend(loc = "upper left")
    graph.grid()
    graph.show()

def main():
    print("Which technology sector stocks have been the best performers throughout the Covid-19 Pandemic?")
    print("Let's analyze the weekly stock performance of 15 tech sector stocks from November 2019 to November 2020...")

    NASDAQ = []
    with open("C:/Users/nicle/PycharmProjects/week 13/ndaq/NDAQ.csv", "r") as csvfile:
        readCSV = csv.reader(csvfile)
        for row in list(readCSV)[1:]:
            NASDAQ.append(float(row[4]))
    csvfile.close()

    csv_file_list = get_csv_files()
    for csv_file in csv_file_list:
        ticker = get_ticker_from_file(csv_file)
        date_list, close_list = get_date_and_price_list_from_csv(csv_file)
        graph_xlist_and_ylist(date_list, close_list, ticker)

        for i in close_list:
            if i > mean(NASDAQ) :
                print(ticker,": This stock's share price beat the NASDAQ average, so it did well during the Covid Pandemic")
            break
    show_graph()
main()