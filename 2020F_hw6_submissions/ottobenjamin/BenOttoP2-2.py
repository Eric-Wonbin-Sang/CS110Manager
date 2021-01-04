#I pledge my honor that I have abided by the Stevens Honor System
#Ben Otto

#This code determines whether or not the inputted date is valid

def main():
    date=input("Enter the date in the format MM/DD/YYYY").split("/")
    year=int(date[2])
    month=int(date[0])
    day=int(date[1])
    if (month==2 and day>28):
        print("The date is invalid")
    elif((month==4 or month==6 or month==9 or month==11)and day>30):
        print("The date is invalid")
    elif(day>31):
        print("The date is invalid")
    else:
        print("The date is valid")
main()