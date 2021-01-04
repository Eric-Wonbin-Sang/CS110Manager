#I pledge my honor I have abided by the Stevens Honor System

#This program will accept a date in the format month/day/year
#It will then determine whether or not the date is valid

def main():
    print("This program determines whether or not an entered date is valid.")
    print("When prompted enter your date in the format month/day/year. Ex: 8/22/2014")
    date = input("Enter the date you would like to validate: ")
    month,day,year= date.split('/')
    month = int(month)
    day = int(day)
    year= int(year)
    date = print(month, "/", day, "/", year)
    if month == 1 and day >= 1 and day <= 31 and year > 0:
        print("Your date is valid.")
    elif month == 2 and day >= 1 and day <= 28 and year > 0:
        print("Your date is valid.")
    elif month == 3 and day >= 1 and day <= 31 and year > 0:
        print("Your date is valid.")
    elif month == 4 and day >= 1 and day <= 30 and year > 0:
        print("Your date is valid.")
    elif month == 5 and day >= 1 and day <= 31 and year > 0:
        print("Your date is valid.")
    elif month == 6 and day >= 1 and day <= 30 and year > 0:
        print("Your date is valid.")
    elif month == 7 and day >= 1 and day <= 31 and year > 0:
        print("Your date is valid.")
    elif month == 8 and day >= 1 and day <= 31 and year > 0:
        print("Your date is valid.")
    elif month == 9 and day >= 1 and day <= 30 and year > 0:
        print("Your date is valid.")
    elif month == 10 and day >= 1 and day <= 31 and year > 0:
        print("Your date is valid.")
    elif month == 11 and day >= 1 and day <= 30 and year > 0:
        print("Your date is valid.")
    elif month == 12 and day >= 1 and day <= 31 and year > 0:
        print("Your date is valid.")
    else:
        print("Your date is invalid.")
main()