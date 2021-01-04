#Kayla Batzer HW 6 P2
#I pledge my honor to abide by the Stevens honor code

def main():
    valid = True
    thirtyOneDayMonths = [1, 3, 5, 7, 8, 10, 12]
    date = input("Enter a date in the form month/day/year: ")

    dateList = date.split("/")
    if len(dateList) != 3:
        valid = False
    else:
        month, day, year = dateList

    month = int(month)
    day = int(day)
    year = int(year)

    if month < 1:
        valid = False
    elif month > 12:
        valid = False
    elif month not in thirtyOneDayMonths and day == 31:
        valid = False
    elif day > 31:
        valid = False
    elif day < 0:
        valid = False
    else:
        valid = True

    if valid:
        print("This date is valid.")
    else:
        print("This date is not valid.")

main()
