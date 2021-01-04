# Catherine Maloney - CS 110 HW6
# I pledge my honor that I have abided by the Stevens honor system.

# Problem Two: Write a program that accepts a date in the form of month/day/year
# and outputs whether or not the date is valid. For example, 7/6/1956 is valid
# but 9/31/2000 is not. (Do you know why??). To simplify the program, you can
# ignore the impact of "leap years." (You can ignore February 29th and leap
# years).

def main():
    date = input("Enter any date (in month/day/year format): ")
    valid_date = True
    long_months = [1, 3, 5, 7, 8, 10, 12]

    list_date = date.split('/')
    if len(list_date) != 3:
        valid_date = False
    else:
        month, day, year = list_date

        try:
            month = int(month)
            day = int(day)
            year = int(year)

            if month > 12 or month < 1 or day > 31 or day < 1 or year < 1:
                valid_date = False
            elif month not in long_months and day == 31:
                valid_date = False

        except:
            valid_date = False

    if valid_date:
        print("This date is valid.")

    else:
        print("This date is not valid.")
main()
