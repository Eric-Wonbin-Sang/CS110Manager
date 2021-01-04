#I pledge my honor that I've abided by the Stevens Honor System- Nicholas DiGiacomo
import math
def main():
    userdate = input("Enter your birthday in the form month/day/year:")
    month,day,year = userdate.split('/')
    month = int(month)
    day = int(day)
    year= int(year)

 
    if year > 2020:
        print("Your age is invalid, sorry.")
    elif month > 12:
        print("Your age is invaild, sorry.")
    elif (month == 1 or month == 3  or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        if day > 31:
            print("Your age is invalid, sorry.")
        else:
            print("Your age is valid")
    elif month == 2 and day > 29:
        print("Your age is invalid, sorry.")
    elif (month == 4 or month == 6 or month == 9 or month == 11):
        if day > 30:
            print("Your age is invalid, sorry,")
        else:
            print("Your age is valid")
    else:
        print("Your age is valid")
   
    


main()
    
        
    
