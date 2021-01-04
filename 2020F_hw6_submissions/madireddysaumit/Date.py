#Saumit Madireddy

#I pledge my honor that I have abided by the Stevens Honor System.

def main():
    is_correct = True
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    date = input("Enter a date in the month/day/year format (xx/xx/xxxx): ")

    date_list = date.split("/")
    if len(date_list) !=3:
        is_correct = False
    else:
        month, day, year = date_list

        try:
            month = int(month)
            day = int(day)
            year = int(year)

            if month > 12 or month < 1 or day > 31 or day < 1 or year < 1:
                is_correct = False
            elif month not in months_with_31_days and day == 31:
                is_correct = False
        except:
            is_correct = False

    if is_correct:
        print("The date", date, "is valid")
    else:
        print("The date", date, "is not valid.")
    

main()
