date=input("Enter date: ")
month, day, year = date.split('/')
month=int(month)
day=int(day)
year=int(year)
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    days=31
elif month==4 or month==6 or month==9 or month==11:
    days=30
elif month==2:
    days=28
if(month<1 or month>12):
    print("Invalid date")
elif(day<1 or day>days):
    print("Invalid date")
elif(month>1 and month<12):
    print("Valid date")
elif(day>1 and day<days):
    print("Valid date")
