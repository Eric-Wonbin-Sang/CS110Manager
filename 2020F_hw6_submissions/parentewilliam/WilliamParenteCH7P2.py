# I pledge my honor to abide by the Stevens honor system

def leap_year_test(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True


def main():
    date_init = str(input("Enter a date in the format month/day/year: "))
    date = date_init.split("/")

    month = int(date[0])
    day = int(date[1])
    year = int(date[2])

    months_31 = [1, 3, 5, 7, 8, 10, 11]

    if year < 0:
        print("Your date", date_init, "is invalid")

    elif month in months_31 and 1 <= day <= 31:
        print("Your date", date_init, "is valid.")

    elif month not in months_31 and month <= 12 and month != 2 and 1 <= day <= 30:
        print("Your date", date_init, "is valid.")

    elif month == 2 and leap_year_test(year) is False and 1 <= day <= 28:
        print("Your date", date_init, "is valid.")

    elif month == 2 and leap_year_test(year) is True and 1 <= day <= 29:
        print("Your date", date_init, "is valid.")

    else:
        print("Your date", date_init, "is invalid")


main()
