# I pledge my honor that I have abided by the Stevens Honor System
# Gabrielle Armetta

# A program that accepts a date in the form of month/day/year
# and outputs whether or not the date is valid

def main():
    date = input("Enter date in form of (mm/dd/yyyy):")
    s = str(date)
    month = int(s[0])
    day = int(s[1])
    year = int(s[2])
    month, day, year = s.split('/')
    if day <= 0:
        return False
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day < 32:
            return True
        else:
            return False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day < 31:
            return True
        else:
            return False
    elif month == 2:
        if day < 29:
            return True
        else:
            return False
    if year > 0 and month > 0 and month < 13 and month == True and day == True:
        print("is valid date")
    else:
        print("date is not a valid date")
main()
