#I pledge my honor that I have abided by the Stevens Honor System
def month_review(month):
    if month > 0 and month <= 12:
        return True
    else:
        return False

def day_review(month, day):
    month_list_31days = [1, 3, 5, 7, 8, 10, 12]
    month_list_30days = [4, 6, 9, 11]
    month_list_28days = 2

    for data in month_list_31days:
        if month == data:
            if day >= 1 and day <= 31:
                return True
            else:
                return False

    for data in month_list_30days:
        if month == data:
            if day >= 1 and day <= 30:
                return True
            else:
                return False
    for data in month_list_28days:
        if month == data:
            if day >= 1 and day <= 28:
                return True
            else:
                 return False

def year_review(year):
    if len(year) >= 1 and len(year) <= 4:
        return True
    else:
        return False

def main():
    date = str(input("Enter the date in mm/dd/yyyy format:"))
    month,day,year = date.split("/")

    month_valid = month_review(int(month))
    day_valid = day_review(int(month),int(day))
    year_valid = year_review(year)

    if month_valid == True and day_valid == True and year_valid == True:
        print("The date",date,"is valid.")
    else:
        print("The date",date,"is not valid.")
main()