#hw6 problem 2
#I pledge my honor that I have abided by the Stevens honor system -Maya O

def main():
    date=input("Please enter a date in month/day/year format: ")
    month,day,year = date.split("/")
    
    month = int(month)
    day = int(day)
    year= int(year)
    
    month30 = [4,6,9,11]
    month31 = [1,3,5,7,8,10,12]

    if month >12:
        print("The entered date is not valid")
    
    elif month == 2:
        if day <= 28:
            print("The entered date is valid")
        else:
            print("The entered date is not valid")

    elif month30:
        if day <=30:
            print("The entered date is valid")
        else:
            print("The entered date is not valid")

    elif month31:
        if day <=31:
            print("The entered date is valid")
        else:
            print("The entered date is not valid")
main()


