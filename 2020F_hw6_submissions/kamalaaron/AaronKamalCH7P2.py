# I pledge that I have abided by the stevens honor code
# Aaron Kamal

def main():
    is_valid = True
    months31days = [1,3,5,6,7,8,10,12]
    formateddate=input("Enter a date in mm/dd/yyyy:")
    formateddate_list = formateddate.split('/')
    if len(formateddate_list) !=3:
        is_valid = False
    else:
        month, day, year= formateddate_list
        try:
            month= int(month)
            day= int(day)
            year= int(year)
            if month > 12 or month < 1 or day > 31 or day < 1 or year < 1:
                is_valid = False
            elif month not in months31days and day == 31:
                is_valid = False
        except:
            is_valid = false
    if is_valid:
        print("That is a valid date.")
    else:
        print("That is not a valid date.")
main()
