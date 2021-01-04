# I pledge my honor that I have abided by the Stevens Honor Code
# Riley Sikorski
def main():
    day = eval(input("Please enter the day (as a number):"))
    month = eval(input("Please enter the month (as a number):"))
    year = eval(input("Please enter the year (as a 4-digit number):"))
    print("The date is ", month, "/", day, "/", year, ".")

    if month == 1 :
        if 0 < day <= 31 :
            print("The date is valid")
        else :
            print("The date is not valid")

    if month == 2 :
        if 0 < day <= 28 :
            print("The date is valid")
        else :
            print("The date is not valid")

    if month == 3 :
        if 0 < day <= 31 :
            print("The date is valid")
        else :
            print("The date is not valid")

    if month == 4 :
        if 0 < day <= 30 :
            print("The date is valid")
        else :
            print("The date is not valid")

    if month == 5 :
        if 0 < day <= 31 :
            print("The date is valid")
        else :
            print("The date is not valid")

    if month == 6 :
        if 0 < day <= 30 :
            print("The date is valid")
        else :
            print("The date is not valid")

    if month == 7 :
        if 0 < day <= 31 :
            print("The date is valid")
        else :
            print("The date is not valid")

    if month == 8 :
        if 0 < day <= 31 :
            print("The date is valid")
        else :
            print("The date is not valid")

    if month == 9 :
        if 0 < day <= 30 :
            print("The date is valid")
        else :
            print("The date is not valid")

    if month == 10 :
        if 0 < day <= 31 :
            print("The date is valid")
        else :
            print("The date is not valid")

    if month == 11 :
        if 0 < day <= 30 :
            print("The date is valid")
        else :
            print("The date is not valid")

    if month == 12 :
        if 0 < day <= 31 :
            print("The date is valid")
        else :
            print("The date is not valid")
    if month < 1 :
        print("The date is not valid")
    if month > 12 :
        print("The date is not valid") 

main()
