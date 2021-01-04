# I pledge my Honor that I have abided by the Stevens Honor System

def date_check():
    print("The following program will program will process whether you properly entered the date")
    print("Please input your date in a month/day/year format")
    print("You can either use 02/02/2001 or 2/2/2001, both formats will be accepted")
    print("This program is optimized to handle Leap Years too!")

    raw_date = str(input("\nPlease input your date here: "))
    date_breakdown = raw_date.split("/")

    month = int(date_breakdown[0])
    day = int(date_breakdown[1])
    year = int(date_breakdown[2])

    months_31 = [1, 3, 5, 7, 8, 10, 12]

    print("\nYour date,", str(raw_date) + ",")

    if month > 12 or month < 1 or day > 31 or day < 0 or year <= 0:
        print("is not valid.")

    elif day <= 30 and month != 2:
        print("is a valid date.")

    elif day <= 29 and month == 2:
        if day == 29 and year % 4 != 0:
            print("is not valid.")
        else:
            print("is a valid date.")

    elif day == 31 and month in months_31:
        print("is a valid date.")


date_check()
