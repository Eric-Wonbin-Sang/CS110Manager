# i pledge my honor i have abided by the stevens honor system

def main():

    month = int(input("Enter a month from 1-12: "))
    day = int(input("Enter a day from 1-31: "))
    year = int(input("Enter a year: "))
    date = print(month,"/",day,"/",year)

    if month == 1 and day >= 1 and day <= 31:
        print("This date is valid")
    elif month == 3 and day >= 1 and day <= 31:
        print("This date is valid")
    elif month == 5 and day >= 1 and day <= 31:
        print("This date is valid")
    elif month == 7 and day >= 1 and day <= 31:
        print("This date is valid")
    elif month == 8 and day >= 1 and day <= 31:
        print("This date is valid")
    elif month == 10 and day >= 1 and day <= 31:
        print("This date is valid")
    elif month == 12 and day >= 1 and day <= 31:
        print("This date is valid")

    elif month == 4 and day >= 1 and day <= 30:
        print("This date is valid")
    elif month == 6 and day >= 1 and day <= 30:
        print("This date is valid")
    elif month == 9 and day >= 1 and day <= 30:
        print("This date is valid")
    elif month == 11 and day >= 1 and day <= 30:
        print("This date is valid")

    elif month == 2 and day >= 1 and day <= 28:
        print("This date is valid")

    else:
        print("This date in not valid")
    

main()
