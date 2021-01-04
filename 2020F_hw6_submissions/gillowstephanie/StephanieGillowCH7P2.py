# Stephanie Gillow
# CS110
# I pledge my honor I have abided by the Stevens honor system.

import datetime


def checkDate(datestring):
    try:
        datetime.datetime.strptime(datestring, '%m/%d/%Y')
    except ValueError:
        raise ValueError("Invalid date, or incorrect format.")


inputdate = input("Enter the date in month/day/year format: ")

checkDate(inputdate)
print("Your date is valid.")
