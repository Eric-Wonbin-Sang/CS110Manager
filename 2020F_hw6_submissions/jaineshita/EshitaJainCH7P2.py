# I pledge my Honor that I have
# abided by the Stevens Honor System.
# Eshita Jain
# program determines date validity

def main():
    isValid = True
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    date = input("Enter date (mm/dd/yyy): ")

    date_list = date.split("/")
    if len(date_list) != 3:
        isValid = False
    else:
        month, day, year = date_list

        try:
            month = int(month)
            day = int(day)
            year = int(year)

            if month > 12 or month < 1 or day > 31 or day < 1 or year < 1:
                isValid = False
            elif month not in months_with_31_days and day == 31:
                isValid = False

        except:
            isValid = False

    if isValid:
        print("\nThe date", date, "is valid!")
    else:
        print("\nThe date", date, "is not valid :(")
main()