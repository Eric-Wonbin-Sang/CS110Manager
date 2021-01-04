# AlvinRadoncicCH7P2_110.py
# I abide by the Stevens Honor Code
# This program accepts a date in the form of month/day/year and outputs whether
# or not the date is valid, all while ignoring the impact of "leap years"

def get_date(month, day, year):

    return (str(month) + "/" + str(day) + "/" + str(year))

def main():

    month = int(input("Enter a month, in integer form: "))
    day = int(input("Enter a day, in integer form: "))
    year = int(input("Enter a year, in integer form: "))

    date = get_date(month, day, year)

    print("\nYour inputted date is:", date)

    if month < 1 or month > 12:
        print("\nYour date is invalid.")
    elif day < 1 or day > 31:
        print("\nYour date is invalid.")
    elif year < 0:
        print("\nYour date is invalid.")
    elif month == 2 and day > 28:
        print("\nYou date is invalid.")
    elif month == 4 or month == 6 or month == 9 or month == 11 and day > 30:
        print("\nYour date is invalid.")
    else:
        print("\nYour date is valid.")

main()

""" The date, 9/31/2000, is invalid because it matches the condition of invalidity in line 28. September cannot have more than 30 days."""