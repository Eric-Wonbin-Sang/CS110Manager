#MatthewMascoloCH7P2.py
#I pledge my honor that I have abided
#by the Stevens Honor System. Matthew Mascolo
#
#This program determines whether a date
#is a valid date.

def main():

    dateEntered = input("Enter a date(month/day/year): ")
    month, day, year = map(int, dateEntered.split('/'))

    if month > 0 and month <= 12 and year > 0: 
        if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            if day > 31 or day < 0:
                print("This is not a valid date.")
            else:
                print("This is a valid date.")
        else:
            if month==4 or month==6 or month==9 or month==11:
                if day > 30 or day < 0:
                    print("This is not a valid date.")
                else:
                    print("This is a valid date.")
            else:
                if month==2:
                    if day > 28 or day < 0:
                        print("This is not a valid date.")
                    else:
                        print("This is a valid date.")
    else:
        print("This is not a valid date.")
            
main()
