#I pledge that I have abided by the Stevens Honor System
#This program takes calendar dates adn says if its valid
#It will take it in the form month/day/year

def main():
    print("You will enter a calendar date")
    print("In the form month/day/year")


    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))
    year = int(input("Enter the year: "))


    if month == 1 and day >= 1 and day <= 31:
        print("The date:", month, "/", day, "/", year, "is correct.")
    elif month == 3 and day >= 1 and day <= 31:
        print("The date:", month, "/", day, "/", year, "is correct.")
    elif month == 5 and day >= 1 and day <= 31:
       print("The date:", month, "/", day, "/", year, "is correct.")
    elif month == 7 and day >= 1 and day <= 31:
       print("The date:", month, "/", day, "/", year, "is correct.")
    elif month == 8 and day >= 1 and day <= 31:
        print("The date:", month, "/", day, "/", year, "is correct.")
    elif month == 10 and day >= 1 and day <= 31:
        print("The date:", month, "/", day, "/", year, "is correct.")
    elif month == 12 and day >= 1 and day <= 31:
        print("The date:", month, "/", day, "/", year, "is correct.")
    elif month == 2 and day >= 1 and day <= 28:
       print("The date:", month, "/", day, "/", year, "is correct.")
    elif month == 4 and day >=1 and day <= 30:
        print("The date:", month, "/", day, "/", year, "is correct.")
    elif month == 6 and day>= 1 and day <= 30:
        print("The date:", month, "/", day, "/", year, "is correct.")
    elif month == 9 and day>= 1 and day<= 30:
        print("The date:", month, "/", day, "/", year, "is correct.")
    elif month == 11 and day >= 1 and day <= 30:
        print("The date:", month, "/", day, "/", year, "is correct.")   
    else:
        print("The date:", month, "/", day, "/", year, "is wrong.")

main() 
    
