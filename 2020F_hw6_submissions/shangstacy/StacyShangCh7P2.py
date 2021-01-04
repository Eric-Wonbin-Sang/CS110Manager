# StacyShangCh7P2.py
# CS 110 A HW 6
# Stacy Shang
# I pledge my honor that I have abided by the Stevens Honor System -Stacy

# This program accepts a date and checks whether or not the date is valid

def main():
    print("This program checks the validity of an inputted date.")

    date = input("Enter the date in the form of dd/mm/yy: ")
    
#    dd, mm, yy = date.split("/")
#    dd = int(dd)
#    mm = int(mm)
#    yy = int(yy)

    inputDate = date.split("/")
    dd = inputDate[0]
    mm = inputDate[1]
    yy = inputDate[2]


    
    if(mm==1 or mm==3 or m==7 or mm==8 or mm==10 or mm==12):
        maxim = 31
    elif(mm==4 or mm==6 or mm==9 or mm==11):
        maxim = 30
    else:
        maxim = 28
    if(mm<1 or mm>12):
        print("Date is invalid")
    elif(dd<1 or dd>maxim):
        print("Date is invalid")
    elif(dd==maxim and mm!=12):
        dd=1
        mm==mm+1
        print("The date is:", dd,mm,yy)
    elif(dd==31 and mm==12):
        dd=1
        mm=1
        yy=yy+1
        print("The date is:", dd,mm,yy)
    else:
        dd=dd+1
        print("The date is:", dd,mm,yy)

main()
