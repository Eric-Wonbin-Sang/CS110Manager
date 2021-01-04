#I pledge my honor that I have abided by the Stevens Honor System. Nathaniel Gee

def main():
    print("This program determines if a date is valid. Ex: 7/6/1956 is considered valid")

    date= input("Enter the date in the day/month/year format: ")
    valid= True
    x=[1,3,5,7,8,10,12]

    list= date.split('/')
    if len(list) != 3:
        valid = False
    else:
        month, day, year = list
        try:
            month = int(month)
            day= int(day)
            year= int(year)

            if month > 12:
                valid=False
            elif month<1:
                valid=False
            elif day> 31:
                valid=False
            elif day < 1:
                valid= False
            elif year < 1:
                valid= False
            elif month not in x and day == 31:
                valid= False
        except:
             valid= False

    if valid:
        print("The date is valid")
    else:
        print("The day is NOT valid")

main()





