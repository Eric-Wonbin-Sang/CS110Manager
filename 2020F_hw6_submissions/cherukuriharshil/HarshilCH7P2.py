# Pledge: I pledge my Honor that I  abide by the Stevens Honor System

def valid_date():
    print("This function tells you whether the date you\n input is valid or invalid")
    is_valid = True
    thirty_one_day_months = [1, 3, 5, 7, 8, 10, 12]
    month = int(input("Enter the month in the format of XX: "))
    day = int(input("Enter the day in the format of XX: "))
    year = int(input("Enter the year in the format of XXXX: "))
    c_list = [month, day, year]

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day <= 31:
            is_valid = True
            print("This is a valid date")
        else:
            is_valid = False
            print("This is not a valid date")

    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day <= 30:
            is_valid = True
            print("This is a valid date")
        else:
            is_valid = False
            print("This is not a valid date")


def main():

    valid_date()

main()
