#i pledge my honor that i have abided by the Stevens Honor System - Rachel Flynn
import os
import csv
import matplotlib.pyplot as plt


def get_csv_file_path_list():
    csv_dir = 'C:/Users/rayf1/Desktop/CS110project' #in zipfile
    csv_file_path_list = []
    for file_path in os.listdir(csv_dir):
        csv_file_path_list.append(csv_dir + '/' + file_path)
    return csv_file_path_list


def get_csv_file_path_list_2():
    csv_dir_2 = 'C:/Users/rayf1/Desktop/communicationsector' #in zipfile
    csv_file_path_list_2 = []
    for file_path_2 in os.listdir(csv_dir_2):
        csv_file_path_list_2.append(csv_dir_2 + '/' + file_path_2)
    return csv_file_path_list_2


def get_csv_file_path_list_3():
    csv_dir_3 = 'C:/Users/rayf1/Desktop/industrialsector' #in zipfile
    csv_file_path_list_3 = []
    for file_path_3 in os.listdir(csv_dir_3):
        csv_file_path_list_3.append(csv_dir_3 + '/' + file_path_3)
    return csv_file_path_list_3


def get_ticker_from_file_path(file_path):
    return file_path.split('/')[-1][:-4]


def get_date_list_and_price_list_from_csv(csv_file_path):
    date_list, close_list = [], []
    with open(csv_file_path) as csv_file:
        row_list = csv.reader(csv_file)
        for row_index, row in enumerate(row_list):
            if row_index != 0:
                date = row[0]
                close = float(row[4])
                date_list.append(date)
                close_list.append(close)
    return date_list, close_list


def graph_x_list_y_list(x_list, y_list, ticker):
    plt.plot(x_list, y_list, label=ticker)


def update_and_show_graph_1():
    ax = plt.gca()
    ax.set_xticks(ax.get_xticks()[::10])
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.xticks(rotation=90)
    plt.title('Stock Performance in the Healthcare Sector from 12.02.2019 to 11.27.2020')
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.grid()
    plt.show()


def update_and_show_graph_2():
    ax = plt.gca()
    ax.set_xticks(ax.get_xticks()[::10])
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.xticks(rotation=90)
    plt.title('Stock Performance in the Communications Sector from 12.02.2019 to 11.27.2020')
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.grid()
    plt.show()


def update_and_show_graph_3():
    ax = plt.gca()
    plt.xlabel('Date')
    ax.set_xticks(ax.get_xticks()[::10])
    plt.ylabel('Closing Price')
    plt.xticks(rotation=90)
    plt.title('Stock Performance in the Industrial Sector from 12.02.2019 to 11.27.2020')
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.grid()
    plt.show()


def main():
    try:
        print("""
        For Healthcare Sector, Please Enter 1
        For Communications Sector, Please Enter 2
        For Industrial Sector, Please Enter 3""")
        print()
        askquestion = int(input("Enter Number: "))
        if askquestion == 1:
            csv_file_path_list = get_csv_file_path_list()
            for csv_file_path in csv_file_path_list:
                ticker = get_ticker_from_file_path(csv_file_path)
                date_list, close_list = get_date_list_and_price_list_from_csv(csv_file_path)
                graph_x_list_y_list(date_list, close_list, ticker)
            update_and_show_graph_1()
        elif askquestion == 2:
            csv_file_path_list_2 = get_csv_file_path_list_2()
            for csv_file_path_2 in csv_file_path_list_2:
                ticker = get_ticker_from_file_path(csv_file_path_2)
                date_list, close_list = get_date_list_and_price_list_from_csv(csv_file_path_2)
                graph_x_list_y_list(date_list, close_list, ticker)
            update_and_show_graph_2()
        elif askquestion == 3:
            csv_file_path_list_3 = get_csv_file_path_list_3()
            for csv_file_path_3 in csv_file_path_list_3:
                ticker = get_ticker_from_file_path(csv_file_path_3)
                date_list, close_list = get_date_list_and_price_list_from_csv(csv_file_path_3)
                graph_x_list_y_list(date_list, close_list, ticker)
            update_and_show_graph_3()
        else:
            print("Error:Invalid Number")
    except ValueError:
        print("Error:Non-numerical character")


main()
