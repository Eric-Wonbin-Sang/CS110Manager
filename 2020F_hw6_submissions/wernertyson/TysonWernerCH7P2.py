#I pledge my honor I have abided by the Stevens Honor System - Tyson Werner

date = input("Please enter a date (month/day/year) to determine its validity: ")
month, day, year = date.split("/")
month = int(month)
day = int(day)
year = int(year)

if month < 1 | month > 12 | day < 1 | day > 31 | year < 0:
    print("not a valid date")

elif month == 2 and day >= 29:
    print("not a valid date")

elif month == 4 and day >= 31:
    print("not a valid date")

elif month == 6 and day >= 31:
    print("not a valid date")

elif month == 9 and day >= 31:
    print("not a valid date")

elif month == 11 and day >= 31:
    print("not a valid date")

else:
    print("this is a valid date")