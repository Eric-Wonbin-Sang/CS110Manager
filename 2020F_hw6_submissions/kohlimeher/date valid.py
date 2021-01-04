#checks validity of a date
def main():
    right = True
    months_with_31days = [1, 3, 5, 7, 8, 10, 12]
    months_with_30days = [4, 6, 9, 11]
    months_with_28days = [2]
    
    date=input("Enter the date(mm/dd/yy format): ")
    mm,dd,yy=date.split('/')

    mm=int(mm)
    dd=int(dd)
    yy=int(yy)
    
    if mm > 12 or mm < 1:
        right = False
    elif dd > 31 or dd < 1:
        right = False
    elif mm not in months_with_31days and dd==31:
        right = False
    elif mm in months_with_28days and dd > 28:
        right = False

        
    if right:
        print("The date", date, "is valid")

    else:
        print("The date", date, "is invalid")

main()
