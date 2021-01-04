# Problem 2
#I pledge my honor that I have abided by the Stevens Honor System
def main():
    month = input("Enter the month: ")
    day = input("Enter the day: ")
    year = input("Enter the year: ")
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        max_value = 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        max_value = 30
    else:
        max_value == 28
    if month < 1 or month > 12:
        print("Date is not valid")
    if day < 1 or day > max_value:
        print("Date is not valid")
    if year > 2020:
        print("Date is not valid")
    else:
        print("Valid Date")
main() 
    
