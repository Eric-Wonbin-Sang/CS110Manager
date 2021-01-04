#I pledge my honor that I have abided by the Stevens Honor System. Jake Roux

def main():
    is_true = True

    m_31_days = [1,3,5,7,8,10,12]

    date = input("Enter your date in the mm/dd/yyyy format:")

    date_list = date.split("/")

    if len(date_list) !=3:
        is_true = False
    else:
        month, day, year = date_list

        try:
            month = int(month)

            day = int(day)

            year = int(year)

            if month > 12 or month < 1 or day > 31 or day < 1 or year < 1 or month == 2 and day >28:
                is_true = False

            elif month not in m_31_days and day <= 31:
                is_true = False

        except:
            is_true = False
    if is_true:
        print("Your date is valid.")
    else:
        print("Your date is invalid, please try again.")

main()

