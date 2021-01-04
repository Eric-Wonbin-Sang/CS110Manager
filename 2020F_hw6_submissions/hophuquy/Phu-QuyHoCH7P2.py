# I pledge my honor that I have abided by the Stevens Honor System
# Problem Two
import math

def main():
    is_valid = True
    thirtyonedaymonths = [1,3,5,7,8,10,12]
    date = input('Enter the date in XX/XX/XXXX format: ')
    date_list = date.split('/')
    if len(date_list) != 3:
        is_valid = False
    else:
        month, day, year = date_list
        try:
            month = int(month)
            day = int(day)
            year = int(year)
            if month > 12 or month < 1 or day > 31 or day <1 or year < 1:
                is_valid = False
            elif month not in thirtyonedaymonths and day == 31:
                is_valid = False
        except:
            is_valid = False
    if is_valid:
        print("That is a valid date.")
    else:
        print("That is not a valid date.")

main()
