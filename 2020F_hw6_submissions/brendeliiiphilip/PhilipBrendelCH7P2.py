#Philip Brendel
#I pledge my honor that I have followed the Stevens Honor code


def checkMonth(month):
    months31 = [1,3,5,7,8,10,12]
    
    if int(month) > 12 or int(month) < 1:
        return False
    if int(month) in months31:
        return 31
        print(31)
    if int(month) == 2:
        return 28
        print(28)
    else:
        return 30
        print(30)

def checkDay(day, month):
    if int(day) in range(1,(int(month))+1):
        return True
    else:
        return False
        
def checkYear(year):
    if len(year) != 2:
        return False

def validDate():
    date = input("Input the date in m/d/y format, (ex. 09/05/02) ")
    date = date.split('/')
    day = date[1]
    month = date[0]
    year = date[2]
    Yearchecked = checkYear(year)
    if Yearchecked == False:
        print("Date is invalid, please try again.")
        print("Your year is invalid")
    else:
        monthChecked = checkMonth(month)
        if monthChecked == False:
            print("Date is invalid, please try again.")
            print("Your month is invalid")
        else:
            dayChecked = checkDay(day, monthChecked)
            if dayChecked == False:
                print("Date is invalid, please try again.")
                print("Your day is invalid.")
            else:
                print("Your date is valid.")
validDate()


    
