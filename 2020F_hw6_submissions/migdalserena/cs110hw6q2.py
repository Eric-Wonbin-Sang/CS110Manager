#serena migdal
#I pledge that i have abided by the stevens honor system

def main():
    iscorrect = True
    months31=[1,3,5,7,8,10,12]
    date=input("enter a date in the month/day/year format: ")

    date_list = date.split("/")
    if len(date_list) !=3:
        iscorrect = False
    else:
        month, day, year = date_list

        try:
            month=int(month)
            day=int(day)
            year=int(year)

            if month > 12 or month < 1 or day > 31 or day < 1 or year < 1:
                iscorrect= False
            elif month not in months31 and day == 31:
                iscorrect = False
        except:
            iscorrect = False
    if iscorrect:
        print("the date", date, "is valid")
    else:
            print("the date ", date, "is invalid")
main()
