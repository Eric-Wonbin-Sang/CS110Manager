#I pledge my honor that I have abided by the Stevens Honors System
def main():
    month = int(input("What is the month in the date?"))
    day = int(input("What is the day in the date?"))
    year = int(input("What is the year in the date?"))
    print ("the date you have entered is",month,"/",day, "/" ,year)
    if month==1 and day>=1 and day<=31:
        print("This date is valid")
    elif month==2 and day>=1 and day<=28:
        print("This date is valid")
    elif month==3 and day>=1 and day<=31:
        print("This date is valid")
    elif month==4 and day>=1 and day<=30:
        print("This date is valid")
    elif month ==5 and day>=1 and day<=31:
        print("This date is valid")
    elif month==6 and day>=1 and day<=30:
        print("This date is valid")
    elif month==7 and day>=1 and day<=31:
        print("This date is valid")
    elif month==8 and day>=1 and day<=31:
        print("This date is valid")
    elif month==9 and day>=1 and day<=30:
        print("This date is valid")
    elif month==10 and day>=1 and day<=31:
        print("This date is valid")
    elif month==11 and day>=1 and day<=30:
        print("This date is valid")
    elif month==12 and day>=1 and day<=31:
        print("This date is valid")
    else:
        print("This date is invalid")
main()