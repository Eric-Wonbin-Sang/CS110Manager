#Sidharth Peri
#CS-110-A
#Honor Code: I pledge in my honor that I have abided by the Stevens Honor System

#A program that accepts a date and outputs whether or not the date is valid

#function that takes in month and day inputs as parameters and checks if based on the month, the day can exist
def validate_date(month, day):    
    validate_yes = "The Date is Valid"
    validate_no = "The Date is Not Valid"
    day = int(day) #convert day from string to int to use in later if statement

    #lists for 3 types of months based on number of days
    twenty_eight_day_months = ['2']
    thirty_day_months = ['4', '6', '9', '11']
    thirty_one_day_months = ['1', '3', '5', '7', '8','10', '12']

    #for loops and nested if statements to check what month type the user input is and
    #then output whether it is valid or not based on the number of days that can exist in that month
    for i in range(len(twenty_eight_day_months)):
        if(twenty_eight_day_months[i] == month):
            if(day <= 28):
                return validate_yes
            else:
                return validate_no

    for i in range(len(thirty_day_months)):
        if(thirty_day_months[i] == month):
            if(day <= 30):
                return validate_yes
            else:
                return validate_no
            
    for i in range(len(thirty_one_day_months)):
        if(thirty_one_day_months[i] == month):
            if(day <= 31):
                return validate_yes
            else:
                return validate_no

def main():
    date = input("Enter the date in the form m/dd/yyyy: ")
    date_month, date_day, date_year = date.split("/") #split date into day, month, year by splitting at /
    
    
    validation = validate_date(date_month, date_day) #call validate_date function and set output equal to validation variable

    print(validation)

main()
