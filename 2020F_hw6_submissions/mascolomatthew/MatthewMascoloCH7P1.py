#MatthewMascoloCH7P1.py
#I pledge my honor that I have abided
#by the Stevens Honor System. Matthew Mascolo
#
#This program calculates BMI and determines
#whether it is in a healthy range.

def main():
    
    weight = eval(input("Enter your weight in pounds: "))
    height = eval(input("Enter your height in inches: "))

    BMI = (weight * 720) / (pow(height, 2))
    BMI = round(BMI, 1)
    
    if BMI > 25:
        print("Your BMI is:", BMI)
        print("This is ABOVE what is considered a healthy range.")
    else:
        if BMI < 19:
            print("Your BMI is:", BMI)
            print("This is BELOW what is considered a healthy range.")
        else:
            print("Your BMI is:", BMI)
            print("This is within a healthy range.")
main()
