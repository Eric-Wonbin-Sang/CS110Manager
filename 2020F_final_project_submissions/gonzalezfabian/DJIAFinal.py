import pandas as pd
import matplotlib.pyplot as plt
import csv


def DJIA_moving_average():
    print("This program calculates several indicators for the DJIA's close.")
    print("")
    print("You will be asked to enter the closing point of the DJIA for today, yesterday, and the previous 18 days")
    print("")
    tday, yday, three_days_ago, four_days_ago, five_days_ago, six_days_ago, seven_days_ago, eight_days_ago, nine_days_ago, ten_days_ago, eleven_days_ago, twelve_days_ago, thirteen_days_ago, fourteen_days_ago, fifteen_days_ago, sixteen_days_ago, seventeen_days_ago, eighteen_days_ago, nineteen_days_ago, twenty_days_ago = eval(input("Enter the closing price today, yesterday, and the previous eighteen days, all separated by commas:"))
    print("")
    twenty_day_mavg = (tday + yday + three_days_ago + four_days_ago + five_days_ago +six_days_ago + seven_days_ago + eight_days_ago + nine_days_ago + ten_days_ago + eleven_days_ago + twelve_days_ago + thirteen_days_ago + fourteen_days_ago + fifteen_days_ago + sixteen_days_ago + seventeen_days_ago + eighteen_days_ago + nineteen_days_ago + twenty_days_ago)/20
    ten_day_mavg = (tday + yday + three_days_ago + four_days_ago + five_days_ago + six_days_ago + seven_days_ago + eight_days_ago + nine_days_ago + ten_days_ago)/10
    five_day_mavg = (tday + yday + three_days_ago + four_days_ago + five_days_ago) / 5
    two_day_mavg = (tday + yday) / 2
    highest_closing_price = (max(tday, yday, three_days_ago, four_days_ago, five_days_ago, six_days_ago, seven_days_ago, eight_days_ago, nine_days_ago, ten_days_ago, eleven_days_ago, twelve_days_ago, thirteen_days_ago, fourteen_days_ago, fifteen_days_ago, sixteen_days_ago, seventeen_days_ago, eighteen_days_ago, nineteen_days_ago, twenty_days_ago))
    lowest_closing_price = (min(tday, yday, three_days_ago, four_days_ago, five_days_ago, six_days_ago, seven_days_ago, eight_days_ago, nine_days_ago, ten_days_ago, eleven_days_ago, twelve_days_ago, thirteen_days_ago, fourteen_days_ago, fifteen_days_ago, sixteen_days_ago, seventeen_days_ago, eighteen_days_ago, nineteen_days_ago, twenty_days_ago))
    spread_of_closing_prices = highest_closing_price - lowest_closing_price
    twenty_day_growth = (tday - twenty_days_ago)/(twenty_days_ago)
    ten_day_growth = (tday - ten_days_ago) / (ten_days_ago)
    five_day_growth = (tday - five_days_ago) / (five_days_ago)
    two_day_growth = (tday - yday) / (yday)
    print("")
    print("The 20-day moving average is:", twenty_day_mavg)
    print("The 10-day moving average is:", ten_day_mavg)
    print("The 5-day moving average is:", five_day_mavg)
    print("The 2-day moving average is:", two_day_mavg)
    print("The highest closing price is:", highest_closing_price)
    print("The lowest closing price is:", lowest_closing_price)
    print("The range of the closing prices is:", spread_of_closing_prices)
    print("The 20-day percent change is:", twenty_day_growth)
    print("The 10-day percent change is:", ten_day_growth)
    print("The 5-day percent change is:", five_day_growth)
    print("The 2-day percent change is:", two_day_growth)



def Trump_CSV():
    with open("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Donald Trump.csv", "r") as Trump_Data:
        reader = csv.reader(Trump_Data)
        for row in reader:
            print(row)
        Trump_Data.close()

def Obama_CSV():
    with open("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Barack Obama.csv", "r") as Obama_Data:
        reader = csv.reader(Obama_Data)
        for row in reader:
            print(row)
        Obama_Data.close()

def Bush43_CSV():
    with open("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George W Bush.csv", "r") as Bush43_Data:
        reader = csv.reader(Bush43_Data)
        for row in reader:
            print(row)
        Bush43_Data.close()

def Clinton_CSV():
    with open("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Bill Clinton.csv", "r") as Clinton_Data:
        reader = csv.reader(Clinton_Data)
        for row in reader:
            print(row)
        Clinton_Data.close()

def Bush41_CSV():
    with open("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George HW Bush.csv", "r") as Bush41_Data:
        reader = csv.reader(Bush41_Data)
        for row in reader:
            print(row)
        Bush41_Data.close()




def Display_Data():
    print("This program will display the performance of the DJIA every month during each presdential administration.")
    print("")
    print("1=H.W.Bush. 2=Clinton. 3=W.Bush. 4=Obama. 5=Trump")
    print("")
    Pres_Selection = input("Select the presidential administration for which you would like to see DJIA performance.")
    print("")
    if Pres_Selection == "1":
        print(Bush41_CSV())
    elif Pres_Selection == "2":
        print(Clinton_CSV())
    elif Pres_Selection == "3":
        print(Bush43_CSV())
    elif Pres_Selection == "4":
        print(Obama_CSV())
    elif Pres_Selection == "5":
        print(Trump_CSV())
    else:
        Display_Data()





def Jan_Obama():
    Jan_Obama_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Barack Obama.csv", header=None)
    Jan_Obama_Data = pd.DataFrame(Jan_Obama_Data.values.reshape(97, 7))
    Jan_Obama_column_names = Jan_Obama_Data[0:1].values[0]
    Jan_Obama_Data2 = Jan_Obama_Data[1:]
    Jan_Obama_Data2.columns = Jan_Obama_Data[0:1].values[0]
    Jan_Obama_Data2.head()
    Jan_Obama_Data3 = Jan_Obama_Data2.iloc[[0, 12, 24, 36, 48, 60, 72, 84], [0, 6]]
    Jan_Obama_Data3['Change %'] = list(map(lambda x: x[:-1], Jan_Obama_Data3['Change %'].values))
    Jan_Obama_Data3['Change %'] = [float(x) for x in Jan_Obama_Data3['Change %'].values]
    Jan_Obama_Data3['Change %'] = Jan_Obama_Data3['Change %'].abs()
    print(Jan_Obama_Data3)
    Jan_Obama_Mean = (Jan_Obama_Data3['Change %'].mean())
    print("Average Movement Under Obama in January:", Jan_Obama_Mean)

def Feb_Obama():
    Feb_Obama_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Barack Obama.csv", header=None)
    Feb_Obama_Data = pd.DataFrame(Feb_Obama_Data.values.reshape(97, 7))
    Feb_Obama_column_names = Feb_Obama_Data[0:1].values[0]
    Feb_Obama_Data2 = Feb_Obama_Data[1:]
    Feb_Obama_Data2.columns = Feb_Obama_Data[0:1].values[0]
    Feb_Obama_Data2.head()
    Feb_Obama_Data3 = Feb_Obama_Data2.iloc[[1, 13, 25, 37, 49, 61, 73, 85], [0, 6]]
    Feb_Obama_Data3['Change %'] = list(map(lambda x: x[:-1], Feb_Obama_Data3['Change %'].values))
    Feb_Obama_Data3['Change %'] = [float(x) for x in Feb_Obama_Data3['Change %'].values]
    Feb_Obama_Data3['Change %'] = Feb_Obama_Data3['Change %'].abs()
    Feb_Obama_Mean = (Feb_Obama_Data3['Change %'].mean())
    print("Average Movement Under Obama in February:", Feb_Obama_Mean)

def Mar_Obama():
    Mar_Obama_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Barack Obama.csv", header=None)
    Mar_Obama_Data = pd.DataFrame(Mar_Obama_Data.values.reshape(97, 7))
    Mar_Obama_column_names = Mar_Obama_Data[0:1].values[0]
    Mar_Obama_Data2 = Mar_Obama_Data[1:]
    Mar_Obama_Data2.columns = Mar_Obama_Data[0:1].values[0]
    Mar_Obama_Data2.head()
    Mar_Obama_Data3 = Mar_Obama_Data2.iloc[[2, 14, 25, 38, 50, 62, 74, 86], [0, 6]]
    Mar_Obama_Data3['Change %'] = list(map(lambda x: x[:-1], Mar_Obama_Data3['Change %'].values))
    Mar_Obama_Data3['Change %'] = [float(x) for x in Mar_Obama_Data3['Change %'].values]
    Mar_Obama_Data3['Change %'] = Mar_Obama_Data3['Change %'].abs()
    Mar_Obama_Mean = (Mar_Obama_Data3['Change %'].mean())
    print("Average Movement Under Obama in March:", Mar_Obama_Mean)

def Apr_Obama():
    Apr_Obama_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Barack Obama.csv", header=None)
    Apr_Obama_Data = pd.DataFrame(Apr_Obama_Data.values.reshape(97, 7))
    Apr_Obama_column_names = Apr_Obama_Data[0:1].values[0]
    Apr_Obama_Data2 = Apr_Obama_Data[1:]
    Apr_Obama_Data2.columns = Apr_Obama_Data[0:1].values[0]
    Apr_Obama_Data2.head()
    Apr_Obama_Data3 = Apr_Obama_Data2.iloc[[3, 15, 27, 39, 51, 63, 75, 87], [0, 6]]
    Apr_Obama_Data3['Change %'] = list(map(lambda x: x[:-1], Apr_Obama_Data3['Change %'].values))
    Apr_Obama_Data3['Change %'] = [float(x) for x in Apr_Obama_Data3['Change %'].values]
    Apr_Obama_Data3['Change %'] = Apr_Obama_Data3['Change %'].abs()
    Apr_Obama_Mean = (Apr_Obama_Data3['Change %'].mean())
    print("Average Movement Under Obama in April:", Apr_Obama_Mean)

def May_Obama():
    May_Obama_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Barack Obama.csv", header=None)
    May_Obama_Data = pd.DataFrame(May_Obama_Data.values.reshape(97, 7))
    May_Obama_column_names = May_Obama_Data[0:1].values[0]
    May_Obama_Data2 = May_Obama_Data[1:]
    May_Obama_Data2.columns = May_Obama_Data[0:1].values[0]
    May_Obama_Data2.head()
    May_Obama_Data3 = May_Obama_Data2.iloc[[4, 16, 28, 40, 52, 64, 76, 88], [0, 6]]
    May_Obama_Data3['Change %'] = list(map(lambda x: x[:-1], May_Obama_Data3['Change %'].values))
    May_Obama_Data3['Change %'] = [float(x) for x in May_Obama_Data3['Change %'].values]
    May_Obama_Data3['Change %'] = May_Obama_Data3['Change %'].abs()
    May_Obama_Mean = (May_Obama_Data3['Change %'].mean())
    print("Average Movement Under Obama in May:", May_Obama_Mean)

def Jun_Obama():
    Jun_Obama_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Barack Obama.csv", header=None)
    Jun_Obama_Data = pd.DataFrame(Jun_Obama_Data.values.reshape(97, 7))
    Jun_Obama_column_names = Jun_Obama_Data[0:1].values[0]
    Jun_Obama_Data2 = Jun_Obama_Data[1:]
    Jun_Obama_Data2.columns = Jun_Obama_Data[0:1].values[0]
    Jun_Obama_Data2.head()
    Jun_Obama_Data3 = Jun_Obama_Data2.iloc[[5, 17, 29, 41, 53, 65, 77, 89], [0, 6]]
    Jun_Obama_Data3['Change %'] = list(map(lambda x: x[:-1], Jun_Obama_Data3['Change %'].values))
    Jun_Obama_Data3['Change %'] = [float(x) for x in Jun_Obama_Data3['Change %'].values]
    Jun_Obama_Data3['Change %'] = Jun_Obama_Data3['Change %'].abs()
    Jun_Obama_Mean = (Jun_Obama_Data3['Change %'].mean())
    print("Average Movement Under Obama in June:", Jun_Obama_Mean)

def Jul_Obama():
    Jul_Obama_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Barack Obama.csv", header=None)
    Jul_Obama_Data = pd.DataFrame(Jul_Obama_Data.values.reshape(97, 7))
    Jul_Obama_column_names = Jul_Obama_Data[0:1].values[0]
    Jul_Obama_Data2 = Jul_Obama_Data[1:]
    Jul_Obama_Data2.columns = Jul_Obama_Data[0:1].values[0]
    Jul_Obama_Data2.head()
    Jul_Obama_Data3 = Jul_Obama_Data2.iloc[[6, 18, 30, 42, 54, 66, 78, 90], [0, 6]]
    Jul_Obama_Data3['Change %'] = list(map(lambda x: x[:-1], Jul_Obama_Data3['Change %'].values))
    Jul_Obama_Data3['Change %'] = [float(x) for x in Jul_Obama_Data3['Change %'].values]
    Jul_Obama_Data3['Change %'] = Jul_Obama_Data3['Change %'].abs()
    Jul_Obama_Mean = (Jul_Obama_Data3['Change %'].mean())
    print("Average Movement Under Obama in July:", Jul_Obama_Mean)

def Aug_Obama():
    Aug_Obama_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Barack Obama.csv", header=None)
    Aug_Obama_Data = pd.DataFrame(Aug_Obama_Data.values.reshape(97, 7))
    Aug_Obama_column_names = Aug_Obama_Data[0:1].values[0]
    Aug_Obama_Data2 = Aug_Obama_Data[1:]
    Aug_Obama_Data2.columns = Aug_Obama_Data[0:1].values[0]
    Aug_Obama_Data2.head()
    Aug_Obama_Data3 = Aug_Obama_Data2.iloc[[7, 19, 31, 43, 55, 67, 79, 91], [0, 6]]
    Aug_Obama_Data3['Change %'] = list(map(lambda x: x[:-1], Aug_Obama_Data3['Change %'].values))
    Aug_Obama_Data3['Change %'] = [float(x) for x in Aug_Obama_Data3['Change %'].values]
    Aug_Obama_Data3['Change %'] = Aug_Obama_Data3['Change %'].abs()
    Aug_Obama_Mean = (Aug_Obama_Data3['Change %'].mean())
    print("Average Movement Under Obama in August:", Aug_Obama_Mean)

def Sep_Obama():
    Sep_Obama_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Barack Obama.csv", header=None)
    Sep_Obama_Data = pd.DataFrame(Sep_Obama_Data.values.reshape(97, 7))
    Sep_Obama_column_names = Sep_Obama_Data[0:1].values[0]
    Sep_Obama_Data2 = Sep_Obama_Data[1:]
    Sep_Obama_Data2.columns = Sep_Obama_Data[0:1].values[0]
    Sep_Obama_Data2.head()
    Sep_Obama_Data3 = Sep_Obama_Data2.iloc[[8, 20, 32, 44, 56, 68, 80, 92], [0, 6]]
    Sep_Obama_Data3['Change %'] = list(map(lambda x: x[:-1], Sep_Obama_Data3['Change %'].values))
    Sep_Obama_Data3['Change %'] = [float(x) for x in Sep_Obama_Data3['Change %'].values]
    Sep_Obama_Data3['Change %'] = Sep_Obama_Data3['Change %'].abs()
    Sep_Obama_Mean = (Sep_Obama_Data3['Change %'].mean())
    print("Average Movement Under Obama in September:", Sep_Obama_Mean)

def Oct_Obama():
    Oct_Obama_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Barack Obama.csv", header=None)
    Oct_Obama_Data = pd.DataFrame(Oct_Obama_Data.values.reshape(97, 7))
    Oct_Obama_column_names = Oct_Obama_Data[0:1].values[0]
    Oct_Obama_Data2 = Oct_Obama_Data[1:]
    Oct_Obama_Data2.columns = Oct_Obama_Data[0:1].values[0]
    Oct_Obama_Data2.head()
    Oct_Obama_Data3 = Oct_Obama_Data2.iloc[[9, 21, 33, 45, 57, 69, 81, 93], [0, 6]]
    Oct_Obama_Data3['Change %'] = list(map(lambda x: x[:-1], Oct_Obama_Data3['Change %'].values))
    Oct_Obama_Data3['Change %'] = [float(x) for x in Oct_Obama_Data3['Change %'].values]
    Oct_Obama_Data3['Change %'] = Oct_Obama_Data3['Change %'].abs()
    Oct_Obama_Mean = (Oct_Obama_Data3['Change %'].mean())
    print("Average Movement Under Obama in October:", Oct_Obama_Mean)

def Nov_Obama():
    Nov_Obama_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Barack Obama.csv", header=None)
    Nov_Obama_Data = pd.DataFrame(Nov_Obama_Data.values.reshape(97, 7))
    Nov_Obama_column_names = Nov_Obama_Data[0:1].values[0]
    Nov_Obama_Data2 = Nov_Obama_Data[1:]
    Nov_Obama_Data2.columns = Nov_Obama_Data[0:1].values[0]
    Nov_Obama_Data2.head()
    Nov_Obama_Data3 = Nov_Obama_Data2.iloc[[10, 22, 34, 46, 58, 70, 82, 94], [0, 6]]
    Nov_Obama_Data3['Change %'] = list(map(lambda x: x[:-1], Nov_Obama_Data3['Change %'].values))
    Nov_Obama_Data3['Change %'] = [float(x) for x in Nov_Obama_Data3['Change %'].values]
    Nov_Obama_Data3['Change %'] = Nov_Obama_Data3['Change %'].abs()
    Nov_Obama_Mean = (Nov_Obama_Data3['Change %'].mean())
    print("Average Movement Under Obama in:", Nov_Obama_Mean)

def Dec_Obama():
    Dec_Obama_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Barack Obama.csv", header=None)
    Dec_Obama_Data = pd.DataFrame(Dec_Obama_Data.values.reshape(97, 7))
    Dec_Obama_column_names = Dec_Obama_Data[0:1].values[0]
    Dec_Obama_Data2 = Dec_Obama_Data[1:]
    Dec_Obama_Data2.columns = Dec_Obama_Data[0:1].values[0]
    Dec_Obama_Data2.head()
    Dec_Obama_Data3 = Dec_Obama_Data2.iloc[[11, 23, 35, 47, 59, 71, 83, 95], [0, 6]]
    Dec_Obama_Data3['Change %'] = list(map(lambda x: x[:-1], Dec_Obama_Data3['Change %'].values))
    Dec_Obama_Data3['Change %'] = [float(x) for x in Dec_Obama_Data3['Change %'].values]
    Dec_Obama_Data3['Change %'] = Dec_Obama_Data3['Change %'].abs()
    Dec_Obama_Mean = (Dec_Obama_Data3['Change %'].mean())
    print("Average Movement Under Obama in:", Dec_Obama_Mean)


def Jan_Trump():
    Jan_Trump_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Donald Trump.csv", header=None)
    Jan_Trump_Data = pd.DataFrame(Jan_Trump_Data.values.reshape(48, 7))
    Jan_Trump_column_names = Jan_Trump_Data[0:1].values[0]
    Jan_Trump_Data2 = Jan_Trump_Data[1:]
    Jan_Trump_Data2.columns = Jan_Trump_Data[0:1].values[0]
    Jan_Trump_Data2.head()
    Jan_Trump_Data3 = Jan_Trump_Data2.iloc[[0, 12, 24, 36], [0, 6]]
    Jan_Trump_Data3['Change %'] = list(map(lambda x: x[:-1], Jan_Trump_Data3['Change %'].values))
    Jan_Trump_Data3['Change %'] = [float(x) for x in Jan_Trump_Data3['Change %'].values]
    Jan_Trump_Data3['Change %'] = Jan_Trump_Data3['Change %'].abs()
    Jan_Trump_Mean = (Jan_Trump_Data3['Change %'].mean())
    print("Average Movement Under Trump in January:", Jan_Trump_Mean)


def Feb_Trump():
    Feb_Trump_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Donald Trump.csv", header=None)
    Feb_Trump_Data = pd.DataFrame(Feb_Trump_Data.values.reshape(48, 7))
    Feb_Trump_column_names = Feb_Trump_Data[0:1].values[0]
    Feb_Trump_Data2 = Feb_Trump_Data[1:]
    Feb_Trump_Data2.columns = Feb_Trump_Data[0:1].values[0]
    Feb_Trump_Data2.head()
    Feb_Trump_Data3 = Feb_Trump_Data2.iloc[[1, 13, 25, 37], [0, 6]]
    Feb_Trump_Data3['Change %'] = list(map(lambda x: x[:-1], Feb_Trump_Data3['Change %'].values))
    Feb_Trump_Data3['Change %'] = [float(x) for x in Feb_Trump_Data3['Change %'].values]
    Feb_Trump_Data3['Change %'] = Feb_Trump_Data3['Change %'].abs()
    Feb_Trump_Mean = (Feb_Trump_Data3['Change %'].mean())
    print("Average Movement Under Trump in February:", Feb_Trump_Mean)


def Mar_Trump():
    Mar_Trump_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Donald Trump.csv", header=None)
    Mar_Trump_Data = pd.DataFrame(Mar_Trump_Data.values.reshape(48, 7))
    Mar_Trump_column_names = Mar_Trump_Data[0:1].values[0]
    Mar_Trump_Data2 = Mar_Trump_Data[1:]
    Mar_Trump_Data2.columns = Mar_Trump_Data[0:1].values[0]
    Mar_Trump_Data2.head()
    Mar_Trump_Data3 = Mar_Trump_Data2.iloc[[2, 14, 25, 38], [0, 6]]
    Mar_Trump_Data3['Change %'] = list(map(lambda x: x[:-1], Mar_Trump_Data3['Change %'].values))
    Mar_Trump_Data3['Change %'] = [float(x) for x in Mar_Trump_Data3['Change %'].values]
    Mar_Trump_Data3['Change %'] = Mar_Trump_Data3['Change %'].abs()
    Mar_Trump_Mean = (Mar_Trump_Data3['Change %'].mean())
    print("Average Movement Under Trump in March:", Mar_Trump_Mean)


def Apr_Trump():
    Apr_Trump_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Donald Trump.csv", header=None)
    Apr_Trump_Data = pd.DataFrame(Apr_Trump_Data.values.reshape(48, 7))
    Apr_Trump_column_names = Apr_Trump_Data[0:1].values[0]
    Apr_Trump_Data2 = Apr_Trump_Data[1:]
    Apr_Trump_Data2.columns = Apr_Trump_Data[0:1].values[0]
    Apr_Trump_Data2.head()
    Apr_Trump_Data3 = Apr_Trump_Data2.iloc[[3, 15, 27, 39], [0, 6]]
    Apr_Trump_Data3['Change %'] = list(map(lambda x: x[:-1], Apr_Trump_Data3['Change %'].values))
    Apr_Trump_Data3['Change %'] = [float(x) for x in Apr_Trump_Data3['Change %'].values]
    Apr_Trump_Data3['Change %'] = Apr_Trump_Data3['Change %'].abs()
    Apr_Trump_Mean = (Apr_Trump_Data3['Change %'].mean())
    print("Average Movement Under Trump in April:", Apr_Trump_Mean)


def May_Trump():
    May_Trump_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Donald Trump.csv", header=None)
    May_Trump_Data = pd.DataFrame(May_Trump_Data.values.reshape(48, 7))
    May_Trump_column_names = May_Trump_Data[0:1].values[0]
    May_Trump_Data2 = May_Trump_Data[1:]
    May_Trump_Data2.columns = May_Trump_Data[0:1].values[0]
    May_Trump_Data2.head()
    May_Trump_Data3 = May_Trump_Data2.iloc[[4, 16, 28, 40], [0, 6]]
    May_Trump_Data3['Change %'] = list(map(lambda x: x[:-1], May_Trump_Data3['Change %'].values))
    May_Trump_Data3['Change %'] = [float(x) for x in May_Trump_Data3['Change %'].values]
    May_Trump_Data3['Change %'] = May_Trump_Data3['Change %'].abs()
    May_Trump_Mean = (May_Trump_Data3['Change %'].mean())
    print("Average Movement Under Trump in May:", May_Trump_Mean)


def Jun_Trump():
    Jun_Trump_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Donald Trump.csv", header=None)
    Jun_Trump_Data = pd.DataFrame(Jun_Trump_Data.values.reshape(48, 7))
    Jun_Trump_column_names = Jun_Trump_Data[0:1].values[0]
    Jun_Trump_Data2 = Jun_Trump_Data[1:]
    Jun_Trump_Data2.columns = Jun_Trump_Data[0:1].values[0]
    Jun_Trump_Data2.head()
    Jun_Trump_Data3 = Jun_Trump_Data2.iloc[[5, 17, 29, 41], [0, 6]]
    Jun_Trump_Data3['Change %'] = list(map(lambda x: x[:-1], Jun_Trump_Data3['Change %'].values))
    Jun_Trump_Data3['Change %'] = [float(x) for x in Jun_Trump_Data3['Change %'].values]
    Jun_Trump_Data3['Change %'] = Jun_Trump_Data3['Change %'].abs()
    Jun_Trump_Mean = (Jun_Trump_Data3['Change %'].mean())
    print("Average Movement Under Trump in June:", Jun_Trump_Mean)


def Jul_Trump():
    Jul_Trump_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Donald Trump.csv", header=None)
    Jul_Trump_Data = pd.DataFrame(Jul_Trump_Data.values.reshape(48, 7))
    Jul_Trump_column_names = Jul_Trump_Data[0:1].values[0]
    Jul_Trump_Data2 = Jul_Trump_Data[1:]
    Jul_Trump_Data2.columns = Jul_Trump_Data[0:1].values[0]
    Jul_Trump_Data2.head()
    Jul_Trump_Data3 = Jul_Trump_Data2.iloc[[6, 18, 30, 42], [0, 6]]
    Jul_Trump_Data3['Change %'] = list(map(lambda x: x[:-1], Jul_Trump_Data3['Change %'].values))
    Jul_Trump_Data3['Change %'] = [float(x) for x in Jul_Trump_Data3['Change %'].values]
    Jul_Trump_Data3['Change %'] = Jul_Trump_Data3['Change %'].abs()
    Jul_Trump_Mean = (Jul_Trump_Data3['Change %'].mean())
    print("Average Movement Under Trump in July:", Jul_Trump_Mean)


def Aug_Trump():
    Aug_Trump_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Donald Trump.csv", header=None)
    Aug_Trump_Data = pd.DataFrame(Aug_Trump_Data.values.reshape(48, 7))
    Aug_Trump_column_names = Aug_Trump_Data[0:1].values[0]
    Aug_Trump_Data2 = Aug_Trump_Data[1:]
    Aug_Trump_Data2.columns = Aug_Trump_Data[0:1].values[0]
    Aug_Trump_Data2.head()
    Aug_Trump_Data3 = Aug_Trump_Data2.iloc[[7, 19, 31, 43], [0, 6]]
    Aug_Trump_Data3['Change %'] = list(map(lambda x: x[:-1], Aug_Trump_Data3['Change %'].values))
    Aug_Trump_Data3['Change %'] = [float(x) for x in Aug_Trump_Data3['Change %'].values]
    Aug_Trump_Data3['Change %'] = Aug_Trump_Data3['Change %'].abs()
    Aug_Trump_Mean = (Aug_Trump_Data3['Change %'].mean())
    print("Average Movement Under Trump in August:", Aug_Trump_Mean)


def Sep_Trump():
    Sep_Trump_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Donald Trump.csv", header=None)
    Sep_Trump_Data = pd.DataFrame(Sep_Trump_Data.values.reshape(48, 7))
    Sep_Trump_column_names = Sep_Trump_Data[0:1].values[0]
    Sep_Trump_Data2 = Sep_Trump_Data[1:]
    Sep_Trump_Data2.columns = Sep_Trump_Data[0:1].values[0]
    Sep_Trump_Data2.head()
    Sep_Trump_Data3 = Sep_Trump_Data2.iloc[[8, 20, 32, 44], [0, 6]]
    Sep_Trump_Data3['Change %'] = list(map(lambda x: x[:-1], Sep_Trump_Data3['Change %'].values))
    Sep_Trump_Data3['Change %'] = [float(x) for x in Sep_Trump_Data3['Change %'].values]
    Sep_Trump_Data3['Change %'] = Sep_Trump_Data3['Change %'].abs()
    Sep_Trump_Mean = (Sep_Trump_Data3['Change %'].mean())
    print("Average Movement Under Trump in September:", Sep_Trump_Mean)


def Oct_Trump():
    Oct_Trump_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Donald Trump.csv", header=None)
    Oct_Trump_Data = pd.DataFrame(Oct_Trump_Data.values.reshape(48, 7))
    Oct_Trump_column_names = Oct_Trump_Data[0:1].values[0]
    Oct_Trump_Data2 = Oct_Trump_Data[1:]
    Oct_Trump_Data2.columns = Oct_Trump_Data[0:1].values[0]
    Oct_Trump_Data2.head()
    Oct_Trump_Data3 = Oct_Trump_Data2.iloc[[9, 21, 33, 45], [0, 6]]
    Oct_Trump_Data3['Change %'] = list(map(lambda x: x[:-1], Oct_Trump_Data3['Change %'].values))
    Oct_Trump_Data3['Change %'] = [float(x) for x in Oct_Trump_Data3['Change %'].values]
    Oct_Trump_Data3['Change %'] = Oct_Trump_Data3['Change %'].abs()
    Oct_Trump_Mean = (Oct_Trump_Data3['Change %'].mean())
    print("Average Movement Under Trump in October:", Oct_Trump_Mean)


def Nov_Trump():
    Nov_Trump_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Donald Trump.csv", header=None)
    Nov_Trump_Data = pd.DataFrame(Nov_Trump_Data.values.reshape(48, 7))
    Nov_Trump_column_names = Nov_Trump_Data[0:1].values[0]
    Nov_Trump_Data2 = Nov_Trump_Data[1:]
    Nov_Trump_Data2.columns = Nov_Trump_Data[0:1].values[0]
    Nov_Trump_Data2.head()
    Nov_Trump_Data3 = Nov_Trump_Data2.iloc[[10, 22, 34, 46], [0, 6]]
    Nov_Trump_Data3['Change %'] = list(map(lambda x: x[:-1], Nov_Trump_Data3['Change %'].values))
    Nov_Trump_Data3['Change %'] = [float(x) for x in Nov_Trump_Data3['Change %'].values]
    Nov_Trump_Data3['Change %'] = Nov_Trump_Data3['Change %'].abs()
    Nov_Trump_Mean = (Nov_Trump_Data3['Change %'].mean())
    print("Average Movement Under Trump in:", Nov_Trump_Mean)


def Dec_Trump():
    Dec_Trump_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Donald Trump.csv", header=None)
    Dec_Trump_Data = pd.DataFrame(Dec_Trump_Data.values.reshape(48, 7))
    Dec_Trump_column_names = Dec_Trump_Data[0:1].values[0]
    Dec_Trump_Data2 = Dec_Trump_Data[1:]
    Dec_Trump_Data2.columns = Dec_Trump_Data[0:1].values[0]
    Dec_Trump_Data2.head()
    Dec_Trump_Data3 = Dec_Trump_Data2.iloc[[11, 23, 35], [0, 6]]
    Dec_Trump_Data3['Change %'] = list(map(lambda x: x[:-1], Dec_Trump_Data3['Change %'].values))
    Dec_Trump_Data3['Change %'] = [float(x) for x in Dec_Trump_Data3['Change %'].values]
    Dec_Trump_Data3['Change %'] = Dec_Trump_Data3['Change %'].abs()
    Dec_Trump_Mean = (Dec_Trump_Data3['Change %'].mean())
    print("Average Movement Under Trump in:", Dec_Trump_Mean)

def Jan_W_Bush():
    Jan_W_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George W Bush.csv", header=None)
    Jan_W_Bush_Data = pd.DataFrame(Jan_W_Bush_Data.values.reshape(97, 7))
    Jan_W_Bush_column_names = Jan_W_Bush_Data[0:1].values[0]
    Jan_W_Bush_Data2 = Jan_W_Bush_Data[1:]
    Jan_W_Bush_Data2.columns = Jan_W_Bush_Data[0:1].values[0]
    Jan_W_Bush_Data2.head()
    Jan_W_Bush_Data3 = Jan_W_Bush_Data2.iloc[[0, 12, 24, 36, 48, 60, 72, 84], [0, 6]]
    Jan_W_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Jan_W_Bush_Data3['Change %'].values))
    Jan_W_Bush_Data3['Change %'] = [float(x) for x in Jan_W_Bush_Data3['Change %'].values]
    Jan_W_Bush_Data3['Change %'] = Jan_W_Bush_Data3['Change %'].abs()
    Jan_W_Bush_Mean = (Jan_W_Bush_Data3['Change %'].mean())
    print("Average Movement Under W_Bush in January:", Jan_W_Bush_Mean)


def Feb_W_Bush():
    Feb_W_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George W Bush.csv", header=None)
    Feb_W_Bush_Data = pd.DataFrame(Feb_W_Bush_Data.values.reshape(97, 7))
    Feb_W_Bush_column_names = Feb_W_Bush_Data[0:1].values[0]
    Feb_W_Bush_Data2 = Feb_W_Bush_Data[1:]
    Feb_W_Bush_Data2.columns = Feb_W_Bush_Data[0:1].values[0]
    Feb_W_Bush_Data2.head()
    Feb_W_Bush_Data3 = Feb_W_Bush_Data2.iloc[[1, 13, 25, 37, 49, 61, 73, 85], [0, 6]]
    Feb_W_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Feb_W_Bush_Data3['Change %'].values))
    Feb_W_Bush_Data3['Change %'] = [float(x) for x in Feb_W_Bush_Data3['Change %'].values]
    Feb_W_Bush_Data3['Change %'] = Feb_W_Bush_Data3['Change %'].abs()
    Feb_W_Bush_Mean = (Feb_W_Bush_Data3['Change %'].mean())
    print("Average Movement Under W_Bush in February:", Feb_W_Bush_Mean)

def Mar_W_Bush():
    Mar_W_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George W Bush.csv", header=None)
    Mar_W_Bush_Data = pd.DataFrame(Mar_W_Bush_Data.values.reshape(97, 7))
    Mar_W_Bush_column_names = Mar_W_Bush_Data[0:1].values[0]
    Mar_W_Bush_Data2 = Mar_W_Bush_Data[1:]
    Mar_W_Bush_Data2.columns = Mar_W_Bush_Data[0:1].values[0]
    Mar_W_Bush_Data2.head()
    Mar_W_Bush_Data3 = Mar_W_Bush_Data2.iloc[[2, 14, 25, 38, 50, 62, 74, 86], [0, 6]]
    Mar_W_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Mar_W_Bush_Data3['Change %'].values))
    Mar_W_Bush_Data3['Change %'] = [float(x) for x in Mar_W_Bush_Data3['Change %'].values]
    Mar_W_Bush_Data3['Change %'] = Mar_W_Bush_Data3['Change %'].abs()
    Mar_W_Bush_Mean = (Mar_W_Bush_Data3['Change %'].mean())
    print("Average Movement Under W_Bush in March:", Mar_W_Bush_Mean)

def Apr_W_Bush():
    Apr_W_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George W Bush.csv", header=None)
    Apr_W_Bush_Data = pd.DataFrame(Apr_W_Bush_Data.values.reshape(97, 7))
    Apr_W_Bush_column_names = Apr_W_Bush_Data[0:1].values[0]
    Apr_W_Bush_Data2 = Apr_W_Bush_Data[1:]
    Apr_W_Bush_Data2.columns = Apr_W_Bush_Data[0:1].values[0]
    Apr_W_Bush_Data2.head()
    Apr_W_Bush_Data3 = Apr_W_Bush_Data2.iloc[[3, 15, 27, 39, 51, 63, 75, 87], [0, 6]]
    Apr_W_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Apr_W_Bush_Data3['Change %'].values))
    Apr_W_Bush_Data3['Change %'] = [float(x) for x in Apr_W_Bush_Data3['Change %'].values]
    Apr_W_Bush_Data3['Change %'] = Apr_W_Bush_Data3['Change %'].abs()
    Apr_W_Bush_Mean = (Apr_W_Bush_Data3['Change %'].mean())
    print("Average Movement Under W_Bush in April:", Apr_W_Bush_Mean)

def May_W_Bush():
    May_W_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George W Bush.csv", header=None)
    May_W_Bush_Data = pd.DataFrame(May_W_Bush_Data.values.reshape(97, 7))
    May_W_Bush_column_names = May_W_Bush_Data[0:1].values[0]
    May_W_Bush_Data2 = May_W_Bush_Data[1:]
    May_W_Bush_Data2.columns = May_W_Bush_Data[0:1].values[0]
    May_W_Bush_Data2.head()
    May_W_Bush_Data3 = May_W_Bush_Data2.iloc[[4, 16, 28, 40, 52, 64, 76, 88], [0, 6]]
    May_W_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], May_W_Bush_Data3['Change %'].values))
    May_W_Bush_Data3['Change %'] = [float(x) for x in May_W_Bush_Data3['Change %'].values]
    May_W_Bush_Data3['Change %'] = May_W_Bush_Data3['Change %'].abs()
    May_W_Bush_Mean = (May_W_Bush_Data3['Change %'].mean())
    print("Average Movement Under W_Bush in May:", May_W_Bush_Mean)

def Jun_W_Bush():
    Jun_W_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George W Bush.csv", header=None)
    Jun_W_Bush_Data = pd.DataFrame(Jun_W_Bush_Data.values.reshape(97, 7))
    Jun_W_Bush_column_names = Jun_W_Bush_Data[0:1].values[0]
    Jun_W_Bush_Data2 = Jun_W_Bush_Data[1:]
    Jun_W_Bush_Data2.columns = Jun_W_Bush_Data[0:1].values[0]
    Jun_W_Bush_Data2.head()
    Jun_W_Bush_Data3 = Jun_W_Bush_Data2.iloc[[5, 17, 29, 41, 53, 65, 77, 89], [0, 6]]
    Jun_W_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Jun_W_Bush_Data3['Change %'].values))
    Jun_W_Bush_Data3['Change %'] = [float(x) for x in Jun_W_Bush_Data3['Change %'].values]
    Jun_W_Bush_Data3['Change %'] = Jun_W_Bush_Data3['Change %'].abs()
    Jun_W_Bush_Mean = (Jun_W_Bush_Data3['Change %'].mean())
    print("Average Movement Under W_Bush in June:", Jun_W_Bush_Mean)

def Jul_W_Bush():
    Jul_W_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George W Bush.csv", header=None)
    Jul_W_Bush_Data = pd.DataFrame(Jul_W_Bush_Data.values.reshape(97, 7))
    Jul_W_Bush_column_names = Jul_W_Bush_Data[0:1].values[0]
    Jul_W_Bush_Data2 = Jul_W_Bush_Data[1:]
    Jul_W_Bush_Data2.columns = Jul_W_Bush_Data[0:1].values[0]
    Jul_W_Bush_Data2.head()
    Jul_W_Bush_Data3 = Jul_W_Bush_Data2.iloc[[6, 18, 30, 42, 54, 66, 78, 90], [0, 6]]
    Jul_W_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Jul_W_Bush_Data3['Change %'].values))
    Jul_W_Bush_Data3['Change %'] = [float(x) for x in Jul_W_Bush_Data3['Change %'].values]
    Jul_W_Bush_Data3['Change %'] = Jul_W_Bush_Data3['Change %'].abs()
    Jul_W_Bush_Mean = (Jul_W_Bush_Data3['Change %'].mean())
    print("Average Movement Under W_Bush in July:", Jul_W_Bush_Mean)

def Aug_W_Bush():
    Aug_W_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George W Bush.csv", header=None)
    Aug_W_Bush_Data = pd.DataFrame(Aug_W_Bush_Data.values.reshape(97, 7))
    Aug_W_Bush_column_names = Aug_W_Bush_Data[0:1].values[0]
    Aug_W_Bush_Data2 = Aug_W_Bush_Data[1:]
    Aug_W_Bush_Data2.columns = Aug_W_Bush_Data[0:1].values[0]
    Aug_W_Bush_Data2.head()
    Aug_W_Bush_Data3 = Aug_W_Bush_Data2.iloc[[7, 19, 31, 43, 55, 67, 79, 91], [0, 6]]
    Aug_W_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Aug_W_Bush_Data3['Change %'].values))
    Aug_W_Bush_Data3['Change %'] = [float(x) for x in Aug_W_Bush_Data3['Change %'].values]
    Aug_W_Bush_Data3['Change %'] = Aug_W_Bush_Data3['Change %'].abs()
    Aug_W_Bush_Mean = (Aug_W_Bush_Data3['Change %'].mean())
    print("Average Movement Under W_Bush in August:", Aug_W_Bush_Mean)

def Sep_W_Bush():
    Sep_W_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George W Bush.csv", header=None)
    Sep_W_Bush_Data = pd.DataFrame(Sep_W_Bush_Data.values.reshape(97, 7))
    Sep_W_Bush_column_names = Sep_W_Bush_Data[0:1].values[0]
    Sep_W_Bush_Data2 = Sep_W_Bush_Data[1:]
    Sep_W_Bush_Data2.columns = Sep_W_Bush_Data[0:1].values[0]
    Sep_W_Bush_Data2.head()
    Sep_W_Bush_Data3 = Sep_W_Bush_Data2.iloc[[8, 20, 32, 44, 56, 68, 80, 92], [0, 6]]
    Sep_W_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Sep_W_Bush_Data3['Change %'].values))
    Sep_W_Bush_Data3['Change %'] = [float(x) for x in Sep_W_Bush_Data3['Change %'].values]
    Sep_W_Bush_Data3['Change %'] = Sep_W_Bush_Data3['Change %'].abs()
    Sep_W_Bush_Mean = (Sep_W_Bush_Data3['Change %'].mean())
    print("Average Movement Under W_Bush in September:", Sep_W_Bush_Mean)

def Oct_W_Bush():
    Oct_W_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George W Bush.csv", header=None)
    Oct_W_Bush_Data = pd.DataFrame(Oct_W_Bush_Data.values.reshape(97, 7))
    Oct_W_Bush_column_names = Oct_W_Bush_Data[0:1].values[0]
    Oct_W_Bush_Data2 = Oct_W_Bush_Data[1:]
    Oct_W_Bush_Data2.columns = Oct_W_Bush_Data[0:1].values[0]
    Oct_W_Bush_Data2.head()
    Oct_W_Bush_Data3 = Oct_W_Bush_Data2.iloc[[9, 21, 33, 45, 57, 69, 81, 93], [0, 6]]
    Oct_W_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Oct_W_Bush_Data3['Change %'].values))
    Oct_W_Bush_Data3['Change %'] = [float(x) for x in Oct_W_Bush_Data3['Change %'].values]
    Oct_W_Bush_Data3['Change %'] = Oct_W_Bush_Data3['Change %'].abs()
    Oct_W_Bush_Mean = (Oct_W_Bush_Data3['Change %'].mean())
    print("Average Movement Under W_Bush in October:", Oct_W_Bush_Mean)

def Nov_W_Bush():
    Nov_W_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George W Bush.csv", header=None)
    Nov_W_Bush_Data = pd.DataFrame(Nov_W_Bush_Data.values.reshape(97, 7))
    Nov_W_Bush_column_names = Nov_W_Bush_Data[0:1].values[0]
    Nov_W_Bush_Data2 = Nov_W_Bush_Data[1:]
    Nov_W_Bush_Data2.columns = Nov_W_Bush_Data[0:1].values[0]
    Nov_W_Bush_Data2.head()
    Nov_W_Bush_Data3 = Nov_W_Bush_Data2.iloc[[10, 22, 34, 46, 58, 70, 82, 94], [0, 6]]
    Nov_W_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Nov_W_Bush_Data3['Change %'].values))
    Nov_W_Bush_Data3['Change %'] = [float(x) for x in Nov_W_Bush_Data3['Change %'].values]
    Nov_W_Bush_Data3['Change %'] = Nov_W_Bush_Data3['Change %'].abs()
    Nov_W_Bush_Mean = (Nov_W_Bush_Data3['Change %'].mean())
    print("Average Movement Under W_Bush in:", Nov_W_Bush_Mean)

def Dec_W_Bush():
    Dec_W_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George W Bush.csv", header=None)
    Dec_W_Bush_Data = pd.DataFrame(Dec_W_Bush_Data.values.reshape(97, 7))
    Dec_W_Bush_column_names = Dec_W_Bush_Data[0:1].values[0]
    Dec_W_Bush_Data2 = Dec_W_Bush_Data[1:]
    Dec_W_Bush_Data2.columns = Dec_W_Bush_Data[0:1].values[0]
    Dec_W_Bush_Data2.head()
    Dec_W_Bush_Data3 = Dec_W_Bush_Data2.iloc[[11, 23, 35, 47, 59, 71, 83, 95], [0, 6]]
    Dec_W_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Dec_W_Bush_Data3['Change %'].values))
    Dec_W_Bush_Data3['Change %'] = [float(x) for x in Dec_W_Bush_Data3['Change %'].values]
    Dec_W_Bush_Data3['Change %'] = Dec_W_Bush_Data3['Change %'].abs()
    Dec_W_Bush_Mean = (Dec_W_Bush_Data3['Change %'].mean())
    print("Average Movement Under W_Bush in:", Dec_W_Bush_Mean)

def Jan_Clinton():
    Jan_Clinton_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Bill Clinton.csv",
                                   header=None)
    Jan_Clinton_Data = pd.DataFrame(Jan_Clinton_Data.values.reshape(97, 7))
    Jan_Clinton_column_names = Jan_Clinton_Data[0:1].values[0]
    Jan_Clinton_Data2 = Jan_Clinton_Data[1:]
    Jan_Clinton_Data2.columns = Jan_Clinton_Data[0:1].values[0]
    Jan_Clinton_Data2.head()
    Jan_Clinton_Data3 = Jan_Clinton_Data2.iloc[[0, 12, 24, 36, 48, 60, 72, 84], [0, 6]]
    Jan_Clinton_Data3['Change %'] = list(map(lambda x: x[:-1], Jan_Clinton_Data3['Change %'].values))
    Jan_Clinton_Data3['Change %'] = [float(x) for x in Jan_Clinton_Data3['Change %'].values]
    Jan_Clinton_Data3['Change %'] = Jan_Clinton_Data3['Change %'].abs()
    Jan_Clinton_Mean = (Jan_Clinton_Data3['Change %'].mean())
    print("Average Movement Under Clinton in January:", Jan_Clinton_Mean)

def Feb_Clinton():
    Feb_Clinton_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Bill Clinton.csv",
                                   header=None)
    Feb_Clinton_Data = pd.DataFrame(Feb_Clinton_Data.values.reshape(97, 7))
    Feb_Clinton_column_names = Feb_Clinton_Data[0:1].values[0]
    Feb_Clinton_Data2 = Feb_Clinton_Data[1:]
    Feb_Clinton_Data2.columns = Feb_Clinton_Data[0:1].values[0]
    Feb_Clinton_Data2.head()
    Feb_Clinton_Data3 = Feb_Clinton_Data2.iloc[[1, 13, 25, 37, 49, 61, 73, 85], [0, 6]]
    Feb_Clinton_Data3['Change %'] = list(map(lambda x: x[:-1], Feb_Clinton_Data3['Change %'].values))
    Feb_Clinton_Data3['Change %'] = [float(x) for x in Feb_Clinton_Data3['Change %'].values]
    Feb_Clinton_Data3['Change %'] = Feb_Clinton_Data3['Change %'].abs()
    Feb_Clinton_Mean = (Feb_Clinton_Data3['Change %'].mean())
    print("Average Movement Under Clinton in February:", Feb_Clinton_Mean)

def Mar_Clinton():
    Mar_Clinton_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Bill Clinton.csv",
                                   header=None)
    Mar_Clinton_Data = pd.DataFrame(Mar_Clinton_Data.values.reshape(97, 7))
    Mar_Clinton_column_names = Mar_Clinton_Data[0:1].values[0]
    Mar_Clinton_Data2 = Mar_Clinton_Data[1:]
    Mar_Clinton_Data2.columns = Mar_Clinton_Data[0:1].values[0]
    Mar_Clinton_Data2.head()
    Mar_Clinton_Data3 = Mar_Clinton_Data2.iloc[[2, 14, 25, 38, 50, 62, 74, 86], [0, 6]]
    Mar_Clinton_Data3['Change %'] = list(map(lambda x: x[:-1], Mar_Clinton_Data3['Change %'].values))
    Mar_Clinton_Data3['Change %'] = [float(x) for x in Mar_Clinton_Data3['Change %'].values]
    Mar_Clinton_Data3['Change %'] = Mar_Clinton_Data3['Change %'].abs()
    Mar_Clinton_Mean = (Mar_Clinton_Data3['Change %'].mean())
    print("Average Movement Under Clinton in March:", Mar_Clinton_Mean)

def Apr_Clinton():
    Apr_Clinton_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Bill Clinton.csv",
                                   header=None)
    Apr_Clinton_Data = pd.DataFrame(Apr_Clinton_Data.values.reshape(97, 7))
    Apr_Clinton_column_names = Apr_Clinton_Data[0:1].values[0]
    Apr_Clinton_Data2 = Apr_Clinton_Data[1:]
    Apr_Clinton_Data2.columns = Apr_Clinton_Data[0:1].values[0]
    Apr_Clinton_Data2.head()
    Apr_Clinton_Data3 = Apr_Clinton_Data2.iloc[[3, 15, 27, 39, 51, 63, 75, 87], [0, 6]]
    Apr_Clinton_Data3['Change %'] = list(map(lambda x: x[:-1], Apr_Clinton_Data3['Change %'].values))
    Apr_Clinton_Data3['Change %'] = [float(x) for x in Apr_Clinton_Data3['Change %'].values]
    Apr_Clinton_Data3['Change %'] = Apr_Clinton_Data3['Change %'].abs()
    Apr_Clinton_Mean = (Apr_Clinton_Data3['Change %'].mean())
    print("Average Movement Under Clinton in April:", Apr_Clinton_Mean)

def May_Clinton():
    May_Clinton_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Bill Clinton.csv",
                                   header=None)
    May_Clinton_Data = pd.DataFrame(May_Clinton_Data.values.reshape(97, 7))
    May_Clinton_column_names = May_Clinton_Data[0:1].values[0]
    May_Clinton_Data2 = May_Clinton_Data[1:]
    May_Clinton_Data2.columns = May_Clinton_Data[0:1].values[0]
    May_Clinton_Data2.head()
    May_Clinton_Data3 = May_Clinton_Data2.iloc[[4, 16, 28, 40, 52, 64, 76, 88], [0, 6]]
    May_Clinton_Data3['Change %'] = list(map(lambda x: x[:-1], May_Clinton_Data3['Change %'].values))
    May_Clinton_Data3['Change %'] = [float(x) for x in May_Clinton_Data3['Change %'].values]
    May_Clinton_Data3['Change %'] = May_Clinton_Data3['Change %'].abs()
    May_Clinton_Mean = (May_Clinton_Data3['Change %'].mean())
    print("Average Movement Under Clinton in May:", May_Clinton_Mean)

def Jun_Clinton():
    Jun_Clinton_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Bill Clinton.csv",
                                   header=None)
    Jun_Clinton_Data = pd.DataFrame(Jun_Clinton_Data.values.reshape(97, 7))
    Jun_Clinton_column_names = Jun_Clinton_Data[0:1].values[0]
    Jun_Clinton_Data2 = Jun_Clinton_Data[1:]
    Jun_Clinton_Data2.columns = Jun_Clinton_Data[0:1].values[0]
    Jun_Clinton_Data2.head()
    Jun_Clinton_Data3 = Jun_Clinton_Data2.iloc[[5, 17, 29, 41, 53, 65, 77, 89], [0, 6]]
    Jun_Clinton_Data3['Change %'] = list(map(lambda x: x[:-1], Jun_Clinton_Data3['Change %'].values))
    Jun_Clinton_Data3['Change %'] = [float(x) for x in Jun_Clinton_Data3['Change %'].values]
    Jun_Clinton_Data3['Change %'] = Jun_Clinton_Data3['Change %'].abs()
    Jun_Clinton_Mean = (Jun_Clinton_Data3['Change %'].mean())
    print("Average Movement Under Clinton in June:", Jun_Clinton_Mean)

def Jul_Clinton():
    Jul_Clinton_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Bill Clinton.csv",
                                   header=None)
    Jul_Clinton_Data = pd.DataFrame(Jul_Clinton_Data.values.reshape(97, 7))
    Jul_Clinton_column_names = Jul_Clinton_Data[0:1].values[0]
    Jul_Clinton_Data2 = Jul_Clinton_Data[1:]
    Jul_Clinton_Data2.columns = Jul_Clinton_Data[0:1].values[0]
    Jul_Clinton_Data2.head()
    Jul_Clinton_Data3 = Jul_Clinton_Data2.iloc[[6, 18, 30, 42, 54, 66, 78, 90], [0, 6]]
    Jul_Clinton_Data3['Change %'] = list(map(lambda x: x[:-1], Jul_Clinton_Data3['Change %'].values))
    Jul_Clinton_Data3['Change %'] = [float(x) for x in Jul_Clinton_Data3['Change %'].values]
    Jul_Clinton_Data3['Change %'] = Jul_Clinton_Data3['Change %'].abs()
    Jul_Clinton_Mean = (Jul_Clinton_Data3['Change %'].mean())
    print("Average Movement Under Clinton in July:", Jul_Clinton_Mean)

def Aug_Clinton():
    Aug_Clinton_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Bill Clinton.csv",
                                   header=None)
    Aug_Clinton_Data = pd.DataFrame(Aug_Clinton_Data.values.reshape(97, 7))
    Aug_Clinton_column_names = Aug_Clinton_Data[0:1].values[0]
    Aug_Clinton_Data2 = Aug_Clinton_Data[1:]
    Aug_Clinton_Data2.columns = Aug_Clinton_Data[0:1].values[0]
    Aug_Clinton_Data2.head()
    Aug_Clinton_Data3 = Aug_Clinton_Data2.iloc[[7, 19, 31, 43, 55, 67, 79, 91], [0, 6]]
    Aug_Clinton_Data3['Change %'] = list(map(lambda x: x[:-1], Aug_Clinton_Data3['Change %'].values))
    Aug_Clinton_Data3['Change %'] = [float(x) for x in Aug_Clinton_Data3['Change %'].values]
    Aug_Clinton_Data3['Change %'] = Aug_Clinton_Data3['Change %'].abs()
    Aug_Clinton_Mean = (Aug_Clinton_Data3['Change %'].mean())
    print("Average Movement Under Clinton in August:", Aug_Clinton_Mean)

def Sep_Clinton():
    Sep_Clinton_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Bill Clinton.csv",
                                   header=None)
    Sep_Clinton_Data = pd.DataFrame(Sep_Clinton_Data.values.reshape(97, 7))
    Sep_Clinton_column_names = Sep_Clinton_Data[0:1].values[0]
    Sep_Clinton_Data2 = Sep_Clinton_Data[1:]
    Sep_Clinton_Data2.columns = Sep_Clinton_Data[0:1].values[0]
    Sep_Clinton_Data2.head()
    Sep_Clinton_Data3 = Sep_Clinton_Data2.iloc[[8, 20, 32, 44, 56, 68, 80, 92], [0, 6]]
    Sep_Clinton_Data3['Change %'] = list(map(lambda x: x[:-1], Sep_Clinton_Data3['Change %'].values))
    Sep_Clinton_Data3['Change %'] = [float(x) for x in Sep_Clinton_Data3['Change %'].values]
    Sep_Clinton_Data3['Change %'] = Sep_Clinton_Data3['Change %'].abs()
    Sep_Clinton_Mean = (Sep_Clinton_Data3['Change %'].mean())
    print("Average Movement Under Clinton in September:", Sep_Clinton_Mean)

def Oct_Clinton():
    Oct_Clinton_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Bill Clinton.csv",
                                   header=None)
    Oct_Clinton_Data = pd.DataFrame(Oct_Clinton_Data.values.reshape(97, 7))
    Oct_Clinton_column_names = Oct_Clinton_Data[0:1].values[0]
    Oct_Clinton_Data2 = Oct_Clinton_Data[1:]
    Oct_Clinton_Data2.columns = Oct_Clinton_Data[0:1].values[0]
    Oct_Clinton_Data2.head()
    Oct_Clinton_Data3 = Oct_Clinton_Data2.iloc[[9, 21, 33, 45, 57, 69, 81, 93], [0, 6]]
    Oct_Clinton_Data3['Change %'] = list(map(lambda x: x[:-1], Oct_Clinton_Data3['Change %'].values))
    Oct_Clinton_Data3['Change %'] = [float(x) for x in Oct_Clinton_Data3['Change %'].values]
    Oct_Clinton_Data3['Change %'] = Oct_Clinton_Data3['Change %'].abs()
    Oct_Clinton_Mean = (Oct_Clinton_Data3['Change %'].mean())
    print("Average Movement Under Clinton in October:", Oct_Clinton_Mean)

def Nov_Clinton():
    Nov_Clinton_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Bill Clinton.csv",
                                   header=None)
    Nov_Clinton_Data = pd.DataFrame(Nov_Clinton_Data.values.reshape(97, 7))
    Nov_Clinton_column_names = Nov_Clinton_Data[0:1].values[0]
    Nov_Clinton_Data2 = Nov_Clinton_Data[1:]
    Nov_Clinton_Data2.columns = Nov_Clinton_Data[0:1].values[0]
    Nov_Clinton_Data2.head()
    Nov_Clinton_Data3 = Nov_Clinton_Data2.iloc[[10, 22, 34, 46, 58, 70, 82, 94], [0, 6]]
    Nov_Clinton_Data3['Change %'] = list(map(lambda x: x[:-1], Nov_Clinton_Data3['Change %'].values))
    Nov_Clinton_Data3['Change %'] = [float(x) for x in Nov_Clinton_Data3['Change %'].values]
    Nov_Clinton_Data3['Change %'] = Nov_Clinton_Data3['Change %'].abs()
    Nov_Clinton_Mean = (Nov_Clinton_Data3['Change %'].mean())
    print("Average Movement Under Clinton in:", Nov_Clinton_Mean)

def Dec_Clinton():
    Dec_Clinton_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/Bill Clinton.csv",
                                   header=None)
    Dec_Clinton_Data = pd.DataFrame(Dec_Clinton_Data.values.reshape(97, 7))
    Dec_Clinton_column_names = Dec_Clinton_Data[0:1].values[0]
    Dec_Clinton_Data2 = Dec_Clinton_Data[1:]
    Dec_Clinton_Data2.columns = Dec_Clinton_Data[0:1].values[0]
    Dec_Clinton_Data2.head()
    Dec_Clinton_Data3 = Dec_Clinton_Data2.iloc[[11, 23, 35, 47, 59, 71, 83, 95], [0, 6]]
    Dec_Clinton_Data3['Change %'] = list(map(lambda x: x[:-1], Dec_Clinton_Data3['Change %'].values))
    Dec_Clinton_Data3['Change %'] = [float(x) for x in Dec_Clinton_Data3['Change %'].values]
    Dec_Clinton_Data3['Change %'] = Dec_Clinton_Data3['Change %'].abs()
    Dec_Clinton_Mean = (Dec_Clinton_Data3['Change %'].mean())
    print("Average Movement Under Clinton in:", Dec_Clinton_Mean)

def Jan_HW_Bush():
    Jan_HW_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George HW Bush.csv", header=None)
    Jan_HW_Bush_Data = pd.DataFrame(Jan_HW_Bush_Data.values.reshape(26, 7))
    Jan_HW_Bush_column_names = Jan_HW_Bush_Data[0:1].values[0]
    Jan_HW_Bush_Data2 = Jan_HW_Bush_Data[1:]
    Jan_HW_Bush_Data2.columns = Jan_HW_Bush_Data[0:1].values[0]
    Jan_HW_Bush_Data2.head()
    Jan_HW_Bush_Data3 = Jan_HW_Bush_Data2.iloc[[0, 12, 24], [0, 6]]
    Jan_HW_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Jan_HW_Bush_Data3['Change %'].values))
    Jan_HW_Bush_Data3['Change %'] = [float(x) for x in Jan_HW_Bush_Data3['Change %'].values]
    Jan_HW_Bush_Data3['Change %'] = Jan_HW_Bush_Data3['Change %'].abs()
    Jan_HW_Bush_Mean = (Jan_HW_Bush_Data3['Change %'].mean())
    print("Average Movement Under HW Bush in January:", Jan_HW_Bush_Mean)


def Feb_HW_Bush():
    Feb_HW_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George HW Bush.csv", header=None)
    Feb_HW_Bush_Data = pd.DataFrame(Feb_HW_Bush_Data.values.reshape(26, 7))
    Feb_HW_Bush_column_names = Feb_HW_Bush_Data[0:1].values[0]
    Feb_HW_Bush_Data2 = Feb_HW_Bush_Data[1:]
    Feb_HW_Bush_Data2.columns = Feb_HW_Bush_Data[0:1].values[0]
    Feb_HW_Bush_Data2.head()
    Feb_HW_Bush_Data3 = Feb_HW_Bush_Data2.iloc[[1, 13], [0, 6]]
    Feb_HW_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Feb_HW_Bush_Data3['Change %'].values))
    Feb_HW_Bush_Data3['Change %'] = [float(x) for x in Feb_HW_Bush_Data3['Change %'].values]
    Feb_HW_Bush_Data3['Change %'] = Feb_HW_Bush_Data3['Change %'].abs()
    Feb_HW_Bush_Mean = (Feb_HW_Bush_Data3['Change %'].mean())
    print("Average Movement Under HW Bush in February:", Feb_HW_Bush_Mean)


def Mar_HW_Bush():
    Mar_HW_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George HW Bush.csv", header=None)
    Mar_HW_Bush_Data = pd.DataFrame(Mar_HW_Bush_Data.values.reshape(26, 7))
    Mar_HW_Bush_column_names = Mar_HW_Bush_Data[0:1].values[0]
    Mar_HW_Bush_Data2 = Mar_HW_Bush_Data[1:]
    Mar_HW_Bush_Data2.columns = Mar_HW_Bush_Data[0:1].values[0]
    Mar_HW_Bush_Data2.head()
    Mar_HW_Bush_Data3 = Mar_HW_Bush_Data2.iloc[[2, 14], [0, 6]]
    Mar_HW_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Mar_HW_Bush_Data3['Change %'].values))
    Mar_HW_Bush_Data3['Change %'] = [float(x) for x in Mar_HW_Bush_Data3['Change %'].values]
    Mar_HW_Bush_Data3['Change %'] = Mar_HW_Bush_Data3['Change %'].abs()
    Mar_HW_Bush_Mean = (Mar_HW_Bush_Data3['Change %'].mean())
    print("Average Movement Under HW Bush in March:", Mar_HW_Bush_Mean)


def Apr_HW_Bush():
    Apr_HW_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George HW Bush.csv", header=None)
    Apr_HW_Bush_Data = pd.DataFrame(Apr_HW_Bush_Data.values.reshape(26, 7))
    Apr_HW_Bush_column_names = Apr_HW_Bush_Data[0:1].values[0]
    Apr_HW_Bush_Data2 = Apr_HW_Bush_Data[1:]
    Apr_HW_Bush_Data2.columns = Apr_HW_Bush_Data[0:1].values[0]
    Apr_HW_Bush_Data2.head()
    Apr_HW_Bush_Data3 = Apr_HW_Bush_Data2.iloc[[3, 15], [0, 6]]
    Apr_HW_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Apr_HW_Bush_Data3['Change %'].values))
    Apr_HW_Bush_Data3['Change %'] = [float(x) for x in Apr_HW_Bush_Data3['Change %'].values]
    Apr_HW_Bush_Data3['Change %'] = Apr_HW_Bush_Data3['Change %'].abs()
    Apr_HW_Bush_Mean = (Apr_HW_Bush_Data3['Change %'].mean())
    print("Average Movement Under HW Bush in April:", Apr_HW_Bush_Mean)


def May_HW_Bush():
    May_HW_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George HW Bush.csv", header=None)
    May_HW_Bush_Data = pd.DataFrame(May_HW_Bush_Data.values.reshape(26, 7))
    May_HW_Bush_column_names = May_HW_Bush_Data[0:1].values[0]
    May_HW_Bush_Data2 = May_HW_Bush_Data[1:]
    May_HW_Bush_Data2.columns = May_HW_Bush_Data[0:1].values[0]
    May_HW_Bush_Data2.head()
    May_HW_Bush_Data3 = May_HW_Bush_Data2.iloc[[4, 16], [0, 6]]
    May_HW_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], May_HW_Bush_Data3['Change %'].values))
    May_HW_Bush_Data3['Change %'] = [float(x) for x in May_HW_Bush_Data3['Change %'].values]
    May_HW_Bush_Data3['Change %'] = May_HW_Bush_Data3['Change %'].abs()
    May_HW_Bush_Mean = (May_HW_Bush_Data3['Change %'].mean())
    print("Average Movement Under HW Bush in May:", May_HW_Bush_Mean)


def Jun_HW_Bush():
    Jun_HW_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George HW Bush.csv", header=None)
    Jun_HW_Bush_Data = pd.DataFrame(Jun_HW_Bush_Data.values.reshape(26, 7))
    Jun_HW_Bush_column_names = Jun_HW_Bush_Data[0:1].values[0]
    Jun_HW_Bush_Data2 = Jun_HW_Bush_Data[1:]
    Jun_HW_Bush_Data2.columns = Jun_HW_Bush_Data[0:1].values[0]
    Jun_HW_Bush_Data2.head()
    Jun_HW_Bush_Data3 = Jun_HW_Bush_Data2.iloc[[5, 17], [0, 6]]
    Jun_HW_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Jun_HW_Bush_Data3['Change %'].values))
    Jun_HW_Bush_Data3['Change %'] = [float(x) for x in Jun_HW_Bush_Data3['Change %'].values]
    Jun_HW_Bush_Data3['Change %'] = Jun_HW_Bush_Data3['Change %'].abs()
    Jun_HW_Bush_Mean = (Jun_HW_Bush_Data3['Change %'].mean())
    print("Average Movement Under HW Bush in June:", Jun_HW_Bush_Mean)


def Jul_HW_Bush():
    Jul_HW_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George HW Bush.csv", header=None)
    Jul_HW_Bush_Data = pd.DataFrame(Jul_HW_Bush_Data.values.reshape(26, 7))
    Jul_HW_Bush_column_names = Jul_HW_Bush_Data[0:1].values[0]
    Jul_HW_Bush_Data2 = Jul_HW_Bush_Data[1:]
    Jul_HW_Bush_Data2.columns = Jul_HW_Bush_Data[0:1].values[0]
    Jul_HW_Bush_Data2.head()
    Jul_HW_Bush_Data3 = Jul_HW_Bush_Data2.iloc[[6, 18], [0, 6]]
    Jul_HW_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Jul_HW_Bush_Data3['Change %'].values))
    Jul_HW_Bush_Data3['Change %'] = [float(x) for x in Jul_HW_Bush_Data3['Change %'].values]
    Jul_HW_Bush_Data3['Change %'] = Jul_HW_Bush_Data3['Change %'].abs()
    Jul_HW_Bush_Mean = (Jul_HW_Bush_Data3['Change %'].mean())
    print("Average Movement Under HW Bush in July:", Jul_HW_Bush_Mean)


def Aug_HW_Bush():
    Aug_HW_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George HW Bush.csv", header=None)
    Aug_HW_Bush_Data = pd.DataFrame(Aug_HW_Bush_Data.values.reshape(26, 7))
    Aug_HW_Bush_column_names = Aug_HW_Bush_Data[0:1].values[0]
    Aug_HW_Bush_Data2 = Aug_HW_Bush_Data[1:]
    Aug_HW_Bush_Data2.columns = Aug_HW_Bush_Data[0:1].values[0]
    Aug_HW_Bush_Data2.head()
    Aug_HW_Bush_Data3 = Aug_HW_Bush_Data2.iloc[[7, 19], [0, 6]]
    Aug_HW_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Aug_HW_Bush_Data3['Change %'].values))
    Aug_HW_Bush_Data3['Change %'] = [float(x) for x in Aug_HW_Bush_Data3['Change %'].values]
    Aug_HW_Bush_Data3['Change %'] = Aug_HW_Bush_Data3['Change %'].abs()
    Aug_HW_Bush_Mean = (Aug_HW_Bush_Data3['Change %'].mean())
    print("Average Movement Under HW Bush in August:", Aug_HW_Bush_Mean)


def Sep_HW_Bush():
    Sep_HW_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George HW Bush.csv", header=None)
    Sep_HW_Bush_Data = pd.DataFrame(Sep_HW_Bush_Data.values.reshape(26, 7))
    Sep_HW_Bush_column_names = Sep_HW_Bush_Data[0:1].values[0]
    Sep_HW_Bush_Data2 = Sep_HW_Bush_Data[1:]
    Sep_HW_Bush_Data2.columns = Sep_HW_Bush_Data[0:1].values[0]
    Sep_HW_Bush_Data2.head()
    Sep_HW_Bush_Data3 = Sep_HW_Bush_Data2.iloc[[8, 20], [0, 6]]
    Sep_HW_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Sep_HW_Bush_Data3['Change %'].values))
    Sep_HW_Bush_Data3['Change %'] = [float(x) for x in Sep_HW_Bush_Data3['Change %'].values]
    Sep_HW_Bush_Data3['Change %'] = Sep_HW_Bush_Data3['Change %'].abs()
    Sep_HW_Bush_Mean = (Sep_HW_Bush_Data3['Change %'].mean())
    print("Average Movement Under HW Bush in September:", Sep_HW_Bush_Mean)


def Oct_HW_Bush():
    Oct_HW_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George HW Bush.csv", header=None)
    Oct_HW_Bush_Data = pd.DataFrame(Oct_HW_Bush_Data.values.reshape(26, 7))
    Oct_HW_Bush_column_names = Oct_HW_Bush_Data[0:1].values[0]
    Oct_HW_Bush_Data2 = Oct_HW_Bush_Data[1:]
    Oct_HW_Bush_Data2.columns = Oct_HW_Bush_Data[0:1].values[0]
    Oct_HW_Bush_Data2.head()
    Oct_HW_Bush_Data3 = Oct_HW_Bush_Data2.iloc[[9, 21], [0, 6]]
    Oct_HW_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Oct_HW_Bush_Data3['Change %'].values))
    Oct_HW_Bush_Data3['Change %'] = [float(x) for x in Oct_HW_Bush_Data3['Change %'].values]
    Oct_HW_Bush_Data3['Change %'] = Oct_HW_Bush_Data3['Change %'].abs()
    Oct_HW_Bush_Mean = (Oct_HW_Bush_Data3['Change %'].mean())
    print("Average Movement Under HW Bush in October:", Oct_HW_Bush_Mean)


def Nov_HW_Bush():
    Nov_HW_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George HW Bush.csv", header=None)
    Nov_HW_Bush_Data = pd.DataFrame(Nov_HW_Bush_Data.values.reshape(26, 7))
    Nov_HW_Bush_column_names = Nov_HW_Bush_Data[0:1].values[0]
    Nov_HW_Bush_Data2 = Nov_HW_Bush_Data[1:]
    Nov_HW_Bush_Data2.columns = Nov_HW_Bush_Data[0:1].values[0]
    Nov_HW_Bush_Data2.head()
    Nov_HW_Bush_Data3 = Nov_HW_Bush_Data2.iloc[[10, 22], [0, 6]]
    Nov_HW_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Nov_HW_Bush_Data3['Change %'].values))
    Nov_HW_Bush_Data3['Change %'] = [float(x) for x in Nov_HW_Bush_Data3['Change %'].values]
    Nov_HW_Bush_Data3['Change %'] = Nov_HW_Bush_Data3['Change %'].abs()
    Nov_HW_Bush_Mean = (Nov_HW_Bush_Data3['Change %'].mean())
    print("Average Movement Under HW Bush in:", Nov_HW_Bush_Mean)


def Dec_HW_Bush():
    Dec_HW_Bush_Data = pd.read_csv("C:/Users/12019/Desktop/Fabian Python/Python Final/Data/George HW Bush.csv", header=None)
    Dec_HW_Bush_Data = pd.DataFrame(Dec_HW_Bush_Data.values.reshape(26, 7))
    Dec_HW_Bush_column_names = Dec_HW_Bush_Data[0:1].values[0]
    Dec_HW_Bush_Data2 = Dec_HW_Bush_Data[1:]
    Dec_HW_Bush_Data2.columns = Dec_HW_Bush_Data[0:1].values[0]
    Dec_HW_Bush_Data2.head()
    Dec_HW_Bush_Data3 = Dec_HW_Bush_Data2.iloc[[11, 23], [0, 6]]
    Dec_HW_Bush_Data3['Change %'] = list(map(lambda x: x[:-1], Dec_HW_Bush_Data3['Change %'].values))
    Dec_HW_Bush_Data3['Change %'] = [float(x) for x in Dec_HW_Bush_Data3['Change %'].values]
    Dec_HW_Bush_Data3['Change %'] = Dec_HW_Bush_Data3['Change %'].abs()
    Dec_HW_Bush_Mean = (Dec_HW_Bush_Data3['Change %'].mean())
    print("Average Movement Under HW Bush in:", Dec_HW_Bush_Mean)


def Single_President():
    print("This program will tell you the average volatility of the Dow Jones Industrial Average in each month, for every presidential administration, since the end of the cold war.")
    print("")
    print("1=H.W.Bush. 2=Clinton. 3=W.Bush. 4=Obama. 5=Trump")
    print("")
    president = input("Select a President by entering his corresponding number:")
    print("")
    if president == "4":
        month = input("Select a month by typing the first 3 letters, with EVERY letter in lowercase:")
        print("")
        if month == "jan":
            Jan_Obama()
        elif month == "feb":
            Feb_Obama()
        elif month == "mar":
            Mar_Obama()
        elif month == "apr":
            Apr_Obama()
        elif month == "may":
            May_Obama()
        elif month == "jun":
            Jun_Obama()
        elif month == "jul":
            Jul_Obama()
        elif month == "aug":
            Aug_Obama()
        elif month == "sep":
            Sep_Obama()
        elif month == "oct":
            Oct_Obama()
        elif month == "nov":
            Nov_Obama()
        elif month == "dec":
            Dec_Obama()
        else:
            Single_President()
    elif president == "5":
        month = input("Select a month by typing the first 3 letters, with EVERY letter in lowercase:")
        print("")
        if month == "jan":
            Jan_Trump()
        elif month == "feb":
            Feb_Trump()
        elif month == "mar":
            Mar_Trump()
        elif month == "apr":
            Apr_Trump()
        elif month == "may":
            May_Trump()
        elif month == "jun":
            Jun_Trump()
        elif month == "jul":
            Jul_Trump()
        elif month == "aug":
            Aug_Trump()
        elif month == "sep":
            Sep_Trump()
        elif month == "oct":
            Oct_Trump()
        elif month == "nov":
            Nov_Trump()
        elif month == "dec":
            Dec_Trump()
        else:
            Single_President()
    elif president == "3":
        month = input("Select a month by typing the first 3 letters, with EVERY letter in lowercase:")
        print("")
        if month == "jan":
            Jan_W_Bush()
        elif month == "feb":
            Feb_W_Bush()
        elif month == "mar":
            Mar_W_Bush()
        elif month == "apr":
            Apr_W_Bush()
        elif month == "may":
            May_W_Bush()
        elif month == "jun":
            Jun_W_Bush()
        elif month == "jul":
            Jul_W_Bush()
        elif month == "aug":
            Aug_W_Bush()
        elif month == "sep":
            Sep_W_Bush()
        elif month == "oct":
            Oct_W_Bush()
        elif month == "nov":
            Nov_W_Bush()
        elif month == "dec":
            Dec_W_Bush()
        else:
            Single_President()
    elif president == "2":
        month = input("Select a month by typing the first 3 letters, with EVERY letter in lowercase:")
        print("")
        if month == "jan":
            Jan_Clinton()
        elif month == "feb":
            Feb_Clinton()
        elif month == "mar":
            Mar_Clinton()
        elif month == "apr":
            Apr_Clinton()
        elif month == "may":
            May_Clinton()
        elif month == "jun":
            Jun_Clinton()
        elif month == "jul":
            Jul_Clinton()
        elif month == "aug":
            Aug_Clinton()
        elif month == "sep":
            Sep_Clinton()
        elif month == "oct":
            Oct_Clinton()
        elif month == "nov":
            Nov_Clinton()
        elif month == "dec":
            Dec_Clinton()
        else:
            Single_President()
    elif president == "1":
        month = input("Select a month by typing the first 3 letters, with EVERY letter in lowercase:")
        print("")
        if month == "jan":
            Jan_HW_Bush()
        elif month == "feb":
            Feb_HW_Bush()
        elif month == "mar":
            Mar_HW_Bush()
        elif month == "apr":
            Apr_HW_Bush()
        elif month == "may":
            May_HW_Bush()
        elif month == "jun":
            Jun_HW_Bush()
        elif month == "jul":
            Jul_HW_Bush()
        elif month == "aug":
            Aug_HW_Bush()
        elif month == "sep":
            Sep_HW_Bush()
        elif month == "oct":
            Oct_HW_Bush()
        elif month == "nov":
            Nov_HW_Bush()
        elif month == "dec":
            Dec_HW_Bush()
        else:
            Single_President()
    else:
        Single_President()

def Ranking():
    print("This program will allow you to select a certain month and see which presidential administration since the end"
          "of the Cold War saw the most volatility on the DJIA.")
    print("")
    month = input("Select a month by typing the first 3 letters, with EVERY letter in lowercase:")
    print("")
    if month == "jan":
        print("The administration of Barack Obama saw the greatest volatility on the DJIA during January.")
        Jan_Obama()
    elif month == "feb":
        print("The administration of Donald Trump saw the greatest volatility on the DJIA during February.")
        Feb_Trump()
    elif month == "mar":
        print("The administration of George W. Bush saw the greatest volatility on the DJIA during March.")
        Mar_W_Bush()
    elif month == "apr":
        print("The administration of George W. Bush saw the greatest volatility on the DJIA during April.")
        Apr_W_Bush()
    elif month == "may":
        print("The administration of George W. Bush saw the greatest volatility on the DJIA during May.")
        May_W_Bush()
    elif month == "jun":
        print("The administration of Bill Clinton saw the greatest volatility on the DJIA during June.")
        Jun_Clinton()
    elif month == "jul":
        print("The administration of Barack Obama saw the greatest volatility on the DJIA during July. ")
        Jul_Obama()
    elif month == "aug":
        print("The administration of George W. Bush saw the greatest volatility on the DJIA during August.")
        Aug_W_Bush()
    elif month == "sep":
        print("The administration of Donald Trump saw the greatest volatility on the DJIA during September.")
        Sep_Trump()
    elif month == "oct":
        print("The administration of Donald Trump saw the greatest volatility on the DJIA during October.")
        Oct_Trump()
    elif month == "nov":
        print("The administration of Donald Trump saw the greatest volatility on the DJIA during November.")
        Nov_Trump()
    elif month == "dec":
        print("The administration of Donald Trump saw the greatest volatility on the DJIA during December.")
        Dec_Trump()
    else:
        Ranking()

def Exit():
    input("Press Enter to Exit.")


def Instructions():
    print("")
    print("This program focuses on 5 presidential administrations since the end of the Cold War: George H.W. Bush, Bill Clinton, George W. Bush, Barack Obama, and Donald Trump.")
    print("")
    print("The data begins at December 1991 (in which the USSR dissolved).")
    print("")
    print("Additionally, this program inclues a tool to find the recent moving average of the DJIA.")
    print("")
    print("This program lets you select one of several options.")
    print("")
    print("1= Display the DJIA monthly data for various presidents.")
    print("")
    print("2=See the average volatility of the Dow Jones Industrial Average for a certain month during a president's administration.")
    print("")
    print("3=See the president whose administration saw the greatest average volatility on the DJIA during a certain month.")
    print("")
    print("4=Recieve a summary of the DJIA's performance over the past 20 days.")
    print("")
    print("5=Exit the program.")

def Execution():
    print("")
    selection = input("Please select 1, 2, 3, 4, or 5:")
    print("")
    if selection == "1":
        Display_Data()
        Execution()
    elif selection == "2":
        Single_President()
        Execution()
    elif selection == "3":
        Ranking()
        Execution()
    elif selection == "4":
        DJIA_moving_average()
        Execution()
    elif selection == "5":
        Exit()
    else:
        print("Please ENTER either 1, 2, 3, 4, or 5:")
        main()

def main():
    Instructions()
    Execution()

main()