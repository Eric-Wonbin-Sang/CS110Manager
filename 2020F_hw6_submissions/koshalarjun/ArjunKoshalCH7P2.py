# This is Arjun Koshal's Homework 6 Problem 2
# I pledge my honor that I have abided by the Stevens Honor System
# This program will accept a date in the form of month/day/year and
# will tell you if the date is valid
# Leap years will be included for all those who asked

def leap_year(year):
    leap = False
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 != 0:
            leap = True
    return leap

def main():
    is_correct = True
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    date = input("Enter a date in the month/day/year format: ")

    date_list = date.split("/")
    if len(date_list) != 3:
        is_correct = False
    else:
        month, day, year = date_list

        try:
            month = int(month)
            day = int(day)
            year = int(year)

            if month > 12 or month < 1 or day > 31 or day < 1 or year < 1:
                is_correct = False
            elif month not in months_with_31_days and day == 31:
                is_correct = False

            if leap_year(year) and month == 2 and day == 30:
                is_correct = False
            elif not leap_year(year) and month == 2 and day > 28:
                is_correct = False
        except:
            is_correct = False

    if is_correct:
        print("The date", date, "is valid")
    else:
        print("The date", date, "is not valid. Please enter another date.")

main()


