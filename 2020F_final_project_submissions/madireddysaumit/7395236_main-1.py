import csv
import matplotlib.pyplot as plt
import yfinance as yf

date_list = []
price_list = []
with open("NFLX.csv") as csv_file:
    for row in list(csv.reader(csv_file))[2:]:
        print()
        print(row[0])
        date_list.append(row[0])
        price_list.append(float(row[4]))

with open("AAPL.csv") as csv_file:
    for row in list(csv.reader(csv_file))[2:]:
        print()
        print(row[0])
        date_list.append(row[0])
        price_list.append(float(row[4]))

with open("DIS.csv") as csv_file:
    for row in list(csv.reader(csv_file))[2:]:
        print()
        print(row[0])
        date_list.append(row[0])
        price_list.append(float(row[4]))

with open("AMZN.csv") as csv_file:
    for row in list(csv.reader(csv_file))[2:]:
        print()
        print(row[0])
        date_list.append(row[0])
        price_list.append(float(row[4]))

def get_date_list_and_price_list_from_csv(NFLX):
    date_list, close_list = [], []
    with open(csv_file_path) as csv_file:
        for row in list(csv.reader(csv_file))[1:]:
            date_list.append(row[0])
            close_list.append(float(row[4]))
        return date_list, close_list

def get_date_list_and_price_list_from_csv(AAPL):
    date_list, close_list = [], []
    with open(csv_file_path) as csv_file:
        for row in list(csv.reader(csv_file))[1:]:
            date_list.append(row[0])
            close_list.append(float(row[4]))
        return date_list, close_list

def get_date_list_and_price_list_from_csv(DIS):
    date_list, close_list = [], []
    with open(csv_file_path) as csv_file:
        for row in list(csv.reader(csv_file))[1:]:
            date_list.append(row[0])
            close_list.append(float(row[4]))
        return date_list, close_list

plt.plot(date_list, price_list)
plt.xlabel("Date")
plt.ylabel("Closing price")
plt.title("Best Streaming Stocks")
plt.xticks(rotation=90)
plt.show()