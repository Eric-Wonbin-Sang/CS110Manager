#################################################################################
# Name       : Matthew Nummy
# Date       : 11/19/2020
# Assignment : Homework 6 - Part 2
# Pledge     : I pledge my honor that I have abided by the Stevens Honor System.
#################################################################################

def date_checker(date): # Returns true if the date is valid, false if not.
    day = int(date[1])
    month = int(date[0])
    if 0 < month <= 12 and 0 < day <= 31:
        if month in [4, 6, 9, 11]:
            if day > 30:
                return 0
            else:
                return 1
        elif month == 2:
            if day > 28:
                return 0
            else:
                return 1
        else:
            if day > 31:
                return 0
            else:
                return 1
    else:
        return 0

def main():
    date = raw_input("Enter a date using the format <month/day/year>: ")
    if date_checker(date.split('/')) == 1:
        print("This is a valid date.")
    else:
        print("This is an invalid date.")
main()