# I pledge my honor that I have abided by the Stevens Honor System.
# Melissa Atmaca

def main():
    isValid = True
    thirtyOneDayMonths = [1, 3, 5, 7, 8, 10, 12]
    date = input("Please enter a date in month/day/year format: ")

    date_list = date.split("/")
    month, day, year = date_list

    month = int(month)
    day = int(day)
    year = int(year)

    if month > 12 or month < 1 or day > 31 or day < 1 or year < 1:
        isValid = False
        print("It's not a valid date.")
    elif month not in thirtyOneDayMonths and day == 31:
        isValid = False
        print("It's not a valid date.")
    else:
        print("It's a valid date.")


main()



  
