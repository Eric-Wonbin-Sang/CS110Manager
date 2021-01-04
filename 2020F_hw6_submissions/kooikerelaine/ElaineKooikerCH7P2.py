#I pledge my Honor I have abided by the Stevens Honor System. Elaine Kooiker

#Problem Two; Write a program that accepts a date in the form of month/day/year and outputs whether or not the date is valid.
#For example, 7/6/1956 is valid but 9/31/2000 is not. (Do you know why??).
#To simplify the program, you can ignore the impact of “leap years”. (You can ignore February 29th and leap years).
def eval_month(month):
    if (1<=month<=12):
        return "true"
    else:
        return "false"

    
def eval_day(month,day):
    if ((month ==2) and (day>=28)):
        return "false"
    elif ((month == 9 or 4 or 6 or 11) and (day>30)):
        return "false"
    elif ((month == 1 or 3 or 5 or 7 or 8 or 10 or 12) and (1<=day<=31)):
          return "true"
    else:
          return "false"
def main():
    date=(input("Enter the date in the form MM/DD/YYYY: "))
    month = int(date[0:2])
    day=int(date[3:5])
    year=date[-4:]
    month_eval=eval_month(month)
    day_eval=eval_day(month,day)
    
    if ((month_eval == "true") and (day_eval=="true")):
        print ("The date is valid.")
    else:
        print("The date is not valid.")
    
main()
