def main():
    date = input("Enter a date in m/d/y format")
    is_correct = True
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]

    date_list = date.split("/")
    if len(date_list) != 3:
        is_correct = False
    else:
        m, d, y = date_list

        try:
            m  = int(m)
            d = int(d)
            y = int(y)

            if m > 12 or m < 1 or d > 31 or d < 1 or y < 1:
                is_correct = False
            elif m not in months_with_31_days and d == 31:
                is_correct = False
        except:
            is_correct = False

    if is_correct:
        print("The date", date, "is valid")
    else:
        print("The date", date, "is not valid.")
main()