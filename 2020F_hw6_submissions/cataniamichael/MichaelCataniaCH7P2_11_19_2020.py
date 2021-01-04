# I, Michael Catania, agree to the Stevens Honor Code
# This program determines whether a certain date is real
def main():
    date = input("Enter a date in month/day/year form:")
    m,d,y = date.split('/')
    mo = int(m)
    day = int(d)
    ye = int(y)
    if(mo==1 or mo==3 or mo==5 or mo==7 or mo==8 or mo==10 or mo==12):
        end=31
    elif(mo==4 or mo==6 or mo==9 or mo==11):
        end=30
    else:
        end=28
    if(mo < 1 or mo > 12):
        print("Date is invalid")
    elif(day < 1 or day > end):
        print("Date is invalid")
    else:
        print("Date is valid")
main()
    

        
    
    
    
