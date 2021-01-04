def checker(datelist):
    longmonths = [1, 3 , 5, 7 , 8 , 10 , 12]
    date = True
    if len(datelist) != 3:
        date = False
    else:
        month , day , year = datelist
        month = int(month)
        day = int(day)
        year = int(year)
        if month > 12 or month < 1 or day < 1 or day > 31 or year < 1:
            date = False
        elif month not in longmonths and day == 31:
            date = False
        elif month == 2 and day > 28:
            date = False

    if date == False:
        print( month,"/",day,"/",year , "is a false date")
    else:
        print( month,"/",day,"/",year, "is a valid date")


def main():
    datelist = []
    x = (input("enter a date seperated by /'s, formatted XX/XX/XXXX : "))
    datelist = x.split("/")
    checker(datelist)

main()