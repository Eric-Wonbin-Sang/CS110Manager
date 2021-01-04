#I pledge my honor that I've abided by the Stevens Honor System-Nicholas DiGiacomo
import math

def main():

    weight = float(input("How much do you weigh in pounds:"))
    height = float(input("How tall are you in inches:"))

    bmi = (weight*720)/height**2

    print(bmi)

    if bmi <= 25 and bmi >= 19:
        print("You're within the healthy range")
    elif bmi > 25:
        print("Your're above the healthy range")
    else:
        print("You're under the healthy range")

        
main()
    
