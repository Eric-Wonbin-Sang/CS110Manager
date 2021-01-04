#I pledge my honor that I have abided by the Stevens Honor System. Jill McDonald
#Problem 2


def validate_date(date):
    lst_date = date.split("/")
    month = int(lst_date[0])
    if month < 1 or month > 12:
        return False

    day = int(lst_date[1])
    if day < 1:
        return False

    if month in ( 1, 3,5,7, 8, 10, 12) and day > 31:
        return False

    if month in ( 4, 6, 9, 11) and day > 30:
        return False

    if month == 2 and day > 28:
        return False

    return True
    
 
def main():
    date = input("Please enter the date: ")
    res = validate_date(date)
    if res:
        print("The date is valid.")
    else:
        print("The date is invalid.")


main()
