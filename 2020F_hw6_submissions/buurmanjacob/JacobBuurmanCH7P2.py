#HW7P2
#By: Jacob Buurman
#I pledge my honor that I have abided by the Stevens Honor System.

# This program will prompt the user to enter a date in the MM/DD/YYYY format
# and say whether the date is valid or not.
def main():
    date = input("What is the date (MM/DD/YYYY)?: ")
    month, day, year = date.split("/")
    month = int(month)
    day = int(day)
    year = int(year)
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        max = 31
    elif (month == 4 or month == 6 or month == 9 or month == 11):
        max = 30
    else:
        max = 28
    if (month < 1 or month > 12):
        print("INVALID DATE")
    elif (day < 1 or day > max):
        print("INVALID DATE")
    else:
        print("VALID DATE")
main()