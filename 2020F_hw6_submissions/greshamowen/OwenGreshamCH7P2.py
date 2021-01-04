# I pledge my honor that I have abided by the Stevens Honor System - Owen Gresham


def isDateValid(date):
    daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dateVals = date.split("/")
    if len(dateVals) != 3:
        print("Invalid date")
        return
    month = int(dateVals[0])
    day = int(dateVals[1])
    year = int(dateVals[2])
    if month < 1 or month > 12:
        print("Invalid date")
        return
    if day < 1 or day > daysPerMonth[month - 1]:
        print("Invalid date")
        return
    if year < 0:
        print("Invalid date")
        return
    print("Date is valid")

def main():
    print("This program accepts a date in the format month/day/year and outputs whether the date is valid.")
    date = input("Enter a date in month/day/year format: ")
    isDateValid(date)


main()
