def main():
    date = input("Enter the date: ")
    mm,dd,yy = date.split('/')
    mm = int(mm)
    dd = int(dd)
    yy = int(yy)
    if(mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
        day = 31
    elif(mm == 4 or mm ==6 or mm == 9 or mm == 11):
        day = 30
    if(mm < 1 or mm > 12):
        print("The date is invalid")
    elif(dd < 1 or dd > day):
        print("The date is invalid")
    else:
        print("The date is valid")

main()



