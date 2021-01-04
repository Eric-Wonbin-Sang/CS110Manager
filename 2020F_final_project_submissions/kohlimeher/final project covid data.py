import csv
import matplotlib.pyplot as plt


def get_legend_from_file_path(file_path):
    return file_path.split(" ")


def graph_x_and_y(x, y, legend):
    plt.plot(x, y, label=legend)


def plotgraph():
    plt.xlabel("Date")
    plt.ylabel("Cases")
    plt.xticks(rotation=90)
    plt.title("Covid Cases in New Jersey")
    plt.legend(loc="upper right")
    plt.grid()
    plt.show()




def plotgraph2():
        plt.xlabel("Date")
        plt.ylabel("Cases")
        plt.xticks(rotation=90)
        plt.title("Effect of COVID in New Jersey Hospitals")
        plt.legend(loc="upper right")
        plt.grid()
        plt.show()



def main():

    csv_file_path = "C:/Users/nitin/Desktop/cs110/new-jersey-history.csv"
    legend = get_legend_from_file_path(csv_file_path)

    date = []
    death = []
    positive = []
    recovered = []
    negative = []
    hospitalizedatm = []
    icuatm = []
    ventilatoratm = []
    with open(csv_file_path) as csv_file:
        row_list = csv.reader(csv_file)
        for row_index, row in enumerate(row_list):
            if row_index != 0:
                date.append(row[0])
                death.append(float(row[3]))
                positive.append(float(row[20]))
                recovered.append(float(row[29]))
                negative.append(float(row[13]))
                ventilatoratm.append(float(row[19]))
                hospitalizedatm.append(float(row[9]))
                icuatm.append(float(row[12]))

    active = [(positive[i] - death[i] - recovered[i]) for i in range(len(date))]

    print(" A graph will pop up. After viewing please close it to view the next graph")

    graph_x_and_y(date, recovered, "recovered cases")
    graph_x_and_y(date, death, "death cases")
    graph_x_and_y(date, active, "active cases")
    plotgraph()


    graph_x_and_y(date, hospitalizedatm, "corona patients in hospital")
    graph_x_and_y(date, icuatm, "corona patients in ICU")
    graph_x_and_y(date, ventilatoratm, "corona patients using ventilators")
    plotgraph2()


main()