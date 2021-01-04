# RachelPotterCH7P2.py
# A program that accepts a date in the form of month/day/year and outputs whether or not the date is valid

def valid_date():
    date = input("Enter the date in the form month/day/year: ")
    month, day, year = date.split("/")
    month = int(month)
    day = int(day)
    year = int(year)
    # Check if the month is valid
    if month > 12 or month < 1:
        print("This date is not valid ")
    # Days less than 1 or days greater than 31 are never valid
    elif day < 1 or day > 31:
        print("This date is not valid")
    # April, June, Sept, and Nov can have up to 30 days
    elif month in {4, 6, 9, 11} and day > 30:
        print("This date is not valid")
    # February can have up to 28 days (in a non-leap year)
    elif month == 2 and day > 28:
        print("This date is not valid")
    # Years can;t be negative, and we want up to the current year.
    elif year < 0 or year > 2020:
        print("This date is not valid")
    else:
        print("This date is valid")


valid_date()

# I pledge my honor that I have abided by the Stevens Honor System
# Rachel Potter
