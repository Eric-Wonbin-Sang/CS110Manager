def main():
    print("This program will determine whether or not a calendar date exists")
    month = int(input("Enter a number that corresponds to the month of your date "))
    day = int(input("Enter a number that corresponds to the day of your date "))
    year = int(input("Enter a number that corresponds to the year of your date"))
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
        print("The date you have provided is invalid. Please try again.")
   

main()
