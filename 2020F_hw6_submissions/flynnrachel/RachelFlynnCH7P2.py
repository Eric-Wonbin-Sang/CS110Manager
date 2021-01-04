#i pledge my honor that I have abided by the Stevens Honor System- Rachel Flynn
def main():
    enterdate = input("Enter the date in the form month/day/year: ")
    month_day_year= enterdate.split("/")
    month=int(month_day_year[0])
    day=int(month_day_year[1])
    year=int(month_day_year[2])
    if (month == 1 or month== 3 or month== 5 or month == 7 or month == 8 or month== 10 or month== 12):
        if (day <= 31):
            print("This is a valid date")
        else:
            print("This date is invalid")
    elif(month == 4 or month == 6 or month == 9 or month == 11):
        if (day <=30):
            print("This is a valid date")
        else:
            print("This date is invalid")
    elif(month == 2):
        if(day<= 28):
            print("This is a valid date")
        else:
            print("This date is invalid")

main()
    
            
