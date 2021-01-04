#1

def BMIC():
    weight = float(input("Please enter your weight in pounds: "))
    height = int(input("Please enter your height in inches: "))
    BMI = (weight * 720) / (height ** 2)
    if BMI > 25:
        print(BMI)
        print("\nyour BMI is above the healthy range")
    elif BMI < 19:
        print(BMI)
        print("\nyour BMI is below the healthy range")
    else:
        print(BMI)
        print("\nyour BMI is within the healthy range")
BMIC()

#2
def validdate():
    date = str(input("please enter a date in the form month/day/year: "))
    datelist = date.split("/")
    month = int(datelist[0])
    day = int(datelist[1])
    year = int(datelist[2])
    if year < 0:
        print("Invalid date")
    else:
        if month < 0 or month > 12:
            print("Invalid date")
        else:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if day >= 32:
                    print("Invalid date")
                else:
                    print("This is a valid date")
            else:
                if day >= 31:
                    print("Invalid date")
                else:
                    print("This is a valid date")
validdate()



