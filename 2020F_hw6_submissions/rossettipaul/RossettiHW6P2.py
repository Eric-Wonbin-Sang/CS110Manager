#I pledge my Honor that I have abided by the Stevens Honor System.
def main():
    date = (input("Enter a date in the form Month/Date/Year"))
    x = date.split('/')
    month = int(x[0])
    day = int(x[1])
    year = int(x[2])
    valid = True
    if(month < 1 or month >12):
        valid = False
    if(day < 1 or day > 31):
        valid = False
    if(month == 2 and day > 28):
        valid = False
    elif(day > 30):
        if(month == 4 or month == 6 or month == 9 or month == 11):
            valid = False
    if(valid):
        print("The date is valid.")
    else:
        print("The date is invalid.")

main()