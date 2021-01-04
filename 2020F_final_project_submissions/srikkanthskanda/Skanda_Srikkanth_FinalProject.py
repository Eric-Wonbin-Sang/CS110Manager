# Skanda Srikkanth
# I pledge my honor that I have abided by the Stevens Honor System

# Microsoft (MSFT) and Apple (AAPL) Stock

"""This program will analyze the open/close, high/low prices of Apple and Microsoft"""
# Question: Which company's stock price was more negatively affected by the COVID pandemic, compared to their performance in 2019?

import csv
from matplotlib import pyplot as plt

print("I will split the data into pre-pandemic and pandemic economies")
print("I will define the pandemic economy as dates on and after Jan 31, which was when the White House declared this a public health emergency")
print()

label = ['MSFT', 'AAPL']
microsoft = "C:/Users/srikk/OneDrive/Documents/CS-110/Data/MSFT_2019-2020.csv"
apple = "C:/Users/srikk/OneDrive/Documents/CS-110/Data/AAPL_2019-2020.csv"

company = ["C:/Users/srikk/OneDrive/Documents/CS-110/Data/MSFT_2019-2020.csv",
           "C:/Users/srikk/OneDrive/Documents/CS-110/Data/AAPL_2019-2020.csv"]


class Apple:

    def normal_graph(self):
        date = []
        variable = []
        with open(apple) as file:
            print("Apple (AAPL):")
            i = input("Enter 'CP' for closing price, 'OCA' for open/close average, and 'HLC' for the high/low change: ")
            if i == 'CP':
                for row in list(csv.reader(file))[1:274]:
                    date.append(row[0])
                    variable.append(float(row[4]))
                plt.plot(date, variable)
                plt.xlabel("Date")
                plt.ylabel("Closing Price")
                plt.title("Apple Closing Price from 1/2/2019 to 1/31/2020")
                # ax = plt.gca()
                # ax.axes.xaxis.set_ticks(x_axis_date)
                plt.xticks(rotation=90)
                plt.xticks(fontsize=2)
                plt.grid()
                plt.show()

            elif i == 'OCA':
                for row in list(csv.reader(file))[1:274]:
                    date.append(row[0])
                    oca = (float(row[1]) + float(row[4])) / 2
                    variable.append(oca)
                plt.plot(date, variable)
                plt.xlabel("Date")
                plt.ylabel("Open/Close Average")
                plt.title("Open/Close Average of Apple from 1/2/2019 to 1/31/2020")
                plt.xticks(rotation=90)
                plt.xticks(fontsize=2)
                plt.grid()
                plt.show()

            elif i == 'HLC':
                for row in list(csv.reader(file))[1:274]:
                    date.append(row[0])
                    hlc = float(row[2]) - float(row[3])
                    variable.append(hlc)
                plt.plot(date, variable)
                plt.xlabel("Date")
                plt.ylabel("High Minus Low")
                plt.title("Change in Daily High and Low Price of Apple from 1/2/2019 to 1/31/2020")
                plt.xticks(rotation=90)
                plt.xticks(fontsize=2)
                plt.grid()
                plt.show()

    def pandemic_graph(self):
        date = []
        variable = []
        with open(apple) as file:
            print("Apple (AAPL):")
            j = input("Enter 'CP' for closing price, 'OCA' for open/close average, and 'HLC' for the high/low change: ")
            if j == 'CP':
                for row in list(csv.reader(file))[274:]:
                    date.append(row[0])
                    variable.append(float(row[4]))
                plt.plot(date, variable)
                plt.xlabel("Date")
                plt.ylabel("Closing Price")
                plt.title("Apple Closing Price from 1/31/2020 to 11/24/2020")
                plt.xticks(rotation=90)
                plt.xticks(fontsize=2)
                plt.grid()
                plt.show()

            elif j == 'OCA':
                for row in list(csv.reader(file))[274:]:
                    date.append(row[0])
                    oca = (float(row[1]) + float(row[4])) / 2
                    variable.append(oca)
                plt.plot(date, variable)
                plt.xlabel("Date")
                plt.ylabel("Open/Close Average")
                plt.title("Open/Close Average of Apple from 1/31/2020 to 11/24/2020")
                plt.xticks(rotation=90)
                plt.xticks(fontsize=2)
                plt.grid()
                plt.show()

            elif j == 'HLC':
                for row in list(csv.reader(file))[274:]:
                    date.append(row[0])
                    hlc = float(row[2]) - float(row[3])
                    variable.append(hlc)
                plt.plot(date, variable)
                plt.xlabel("Date")
                plt.ylabel("High Minus Low")
                plt.title("Change in High and Low Price of Apple from 1/31/2020 to 11/24/2020")
                plt.xticks(rotation=90)
                plt.xticks(fontsize=2)
                plt.grid()
                plt.show()


class Microsoft:

    def normal_graph(self):
        date = []
        variable = []
        with open(microsoft) as file:
            print("Microsoft (MSFT):")
            i = input("Enter 'CP' for closing price, 'OCA' for open/close average, and 'HLC' for the high/low change: ")
            if i == 'CP':
                for row in list(csv.reader(file))[1:274]:
                    date.append(row[0])
                    variable.append(float(row[4]))
                plt.plot(date, variable)
                plt.xlabel("Date")
                plt.ylabel("Closing Price")
                plt.title("Microsoft Closing Price from 1/2/2019 to 1/31/2020")
                plt.xticks(rotation=90)
                plt.xticks(fontsize=2)
                plt.grid()
                plt.show()

            elif i == 'OCA':
                for row in list(csv.reader(file))[1:274]:
                    date.append(row[0])
                    oca = (float(row[1]) + float(row[4])) / 2
                    variable.append(oca)
                plt.plot(date, variable)
                plt.xlabel("Date")
                plt.ylabel("Open/Close Average")
                plt.title("Open/Close Average of Microsoft from 1/2/2019 to 1/31/2020")
                plt.xticks(rotation=90)
                plt.xticks(fontsize=2)
                plt.grid()
                plt.show()

            elif i == 'HLC':
                for row in list(csv.reader(file))[1:274]:
                    date.append(row[0])
                    hlc = float(row[2]) - float(row[3])
                    variable.append(hlc)
                plt.plot(date, variable)
                plt.xlabel("Date")
                plt.ylabel("High Minus Low")
                plt.title("Change in Daily High and Low Price of Microsoft from 1/2/2019 to 1/31/2020")
                plt.xticks(rotation=90)
                plt.xticks(fontsize=2)
                plt.grid()
                plt.show()


    def pandemic_graph(self):
        date = []
        variable = []
        with open(microsoft) as file:
            print("Microsoft (MSFT):")
            i = input("Enter 'CP' for closing price, 'OCA' for open/close average, and 'HLC' for the high/low change: ")
            if i == 'CP':
                for row in list(csv.reader(file))[274:]:
                    date.append(row[0])
                    variable.append(float(row[4]))
                plt.plot(date, variable)
                plt.xlabel("Date")
                plt.ylabel("Closing Price")
                plt.title("Microsoft Closing Price from 1/31/2020 to 11/24/2020")
                plt.xticks(rotation=90)
                plt.xticks(fontsize=2)
                plt.grid()
                plt.show()

            elif i == 'OCA':
                for row in list(csv.reader(file))[274:]:
                    date.append(row[0])
                    oca = (float(row[1]) + float(row[4])) / 2
                    variable.append(oca)
                plt.plot(date, variable)
                plt.xlabel("Date")
                plt.ylabel("Open/Close Average")
                plt.title("Open/Close Average of Microsoft from 1/31/2020 to 11/24/2020")
                plt.xticks(rotation=90)
                plt.xticks(fontsize=2)
                plt.grid()
                plt.show()

            elif i == 'HLC':
                for row in list(csv.reader(file))[274:]:
                    date.append(row[0])
                    hlc = float(row[2]) - float(row[3])
                    variable.append(hlc)
                plt.plot(date, variable)
                plt.xlabel("Date")
                plt.ylabel("High Minus Low")
                plt.title("Change in Daily High and Low Price of Microsoft from 1/31/2020 to 11/24/2020")
                plt.xticks(rotation=90)
                plt.xticks(fontsize=2)
                plt.grid()
                plt.show()


def main_graph():
    count = 0
    for file in company:
        date = []
        closing_price = []
        with open(file) as csv_file:
            for row in list(csv.reader(csv_file))[1:]:
                date.append(row[0])
                closing_price.append(float(row[4]))
            plt.plot(date, closing_price, label=label[count])
            count = count + 1

    plt.plot(date, closing_price)
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.title("Closing Price of Apple and Microsoft from 1/2/2019 to 11/24/2020")
    plt.xticks(rotation=90)
    plt.xticks(fontsize=2)
    plt.legend(loc = 'upper left')
    plt.grid()
    plt.show()



# Apple.normal_graph(Apple)
# Apple.pandemic_graph(Apple)
# Microsoft.normal_graph(Microsoft)
# Microsoft.pandemic_graph(Microsoft)
# main_graph()
