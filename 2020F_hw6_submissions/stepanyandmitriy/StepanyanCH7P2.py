#StepanyanCH7P2.py
#I pledge my honor that I have abided by the Stevens Honor System
#This program evaluates the acceptability of dates

def main():
    date = input("Input the date separated by forward slashes(/): ")
    datesplit = date.split("/")
    temp = [int(i) for i in datesplit]

    if temp[0] == 1:
        if 1 <= temp[1] <= 31:
            print("The date", date, "is valid.")
        else:
            print("The date", date, "is invalid.")
    elif temp[0] == 2:
        if 1 <= temp[1] <= 28:
            print("The date", date, "is valid.")
        else:
            print("The date", date, "is invalid.")
    elif temp[0] == 3:
        if 1 <= temp[1] <= 31:
            print("The date", date, "is valid.")
        else:
            print("The date", date, "is invalid.")
    elif temp[0] == 4:
        if 1 <= temp[1] <= 30:
            print("The date", date, "is valid.")
        else:
            print("The date", date, "is invalid.")
    elif temp[0] == 5:
        if 1 <= temp[1] <= 31:
            print("The date", date, "is valid.")
        else:
            print("The date", date, "is invalid.")
    elif temp[0] == 6:
        if 1 <= temp[1] <= 30:
            print("The date", date, "is valid.")
        else:
            print("The date", date, "is invalid.")
    elif temp[0] == 7:
        if 1 <= temp[1] <= 31:
            print("The date", date, "is valid.")
        else:
            print("The date", date, "is invalid.")
    elif temp[0] == 8:
        if 1 <= temp[1] <= 31:
            print("The date", date, "is valid.")
        else:
            print("The date", date, "is invalid.")
    elif temp[0] == 9:
        if 1 <= temp[1] <= 30:
            print("The date", date, "is valid.")
        else:
            print("The date", date, "is invalid.")
    elif temp[0] == 10:
        if 1 <= temp[1] <= 31:
            print("The date", date, "is valid.")
        else:
            print("The date", date, "is invalid.")
    elif temp[0] == 11:
        if 1 <= temp[1] <= 30:
            print("The date", date, "is valid.")
        else:
            print("The date", date, "is invalid.")
    elif temp[0] == 12:
        if 1 <= temp[1] <= 31:
            print("The date", date, "is valid.")
        else:
            print("The date", date, "is invalid.")
    else:
        print("The date", date, "is invalid.")
main()