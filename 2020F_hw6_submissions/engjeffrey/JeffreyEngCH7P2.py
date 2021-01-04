# I pledge my honor that I have abided by the Stevens Honor System.
# Jeffrey Eng

def main():
    x = str(input("Enter a date in the form month/day/year: "))
    date = x.split("/")
    thirty_one = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]
    twenty_eight = [2]
    if int(date[0]) in thirty_one and int(date[1]) <= 31:
        print("Valid date")
    elif int(date[0]) in thirty and int(date[1]) <= 30:
        print("Valid date")
    elif int(date[0]) in twenty_eight and int(date[1]) <= 28:
        print("Valid date")
    else:
        print("Invalid date")
main()
