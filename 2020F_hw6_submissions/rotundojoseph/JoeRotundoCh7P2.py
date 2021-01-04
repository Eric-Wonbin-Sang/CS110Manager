#Date Validity
#HW6q2
#I pledge my honor that I have abided by the Stevens Honor System

def main():
    date = input("Enter a date in the form (MM/DD/YYYY): ")
    month, date, year = date.split('/')
    month = int(month)
    date = int(date)
    year = int(year)
    if month == 11 or month == 4 or month == 6 or month == 9:
        if 1<= date <= 30 and year > 0:
            print("This date is valid.")
        else:
            print("This date is INVALID!")
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if 1 <= date <= 31 and year > 0:
            print("This date is valid.")
        else:
            print("This date is INVALID!")
    if month == 2:
        if 1 <= date <= 28 and year > 0:
            print("This date is valid.")
        else:
            print("This date is INVALID!")
            
main()
