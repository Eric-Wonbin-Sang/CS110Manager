# RachelPotterCH7P1.py
# A program that calculates a person's BMI and determines if it is in a healthy range


def get_bmi():
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    bmi = (weight * 720)/(height**2)
    print("Your BMI is", round(bmi, 2))  # Round to 2 decimal places to avoid super long integers
    if 19 <= bmi <= 25:
        print("Your BMI is in the healthy range!")
    elif bmi < 19:
        print("Your BMI is below the healthy range.")
    else:  # If BMI > 25
        print("Your BMI is above the healthy range.")


get_bmi()

# I pledge my honor that I have abided by the Stevens Honor System
# Rachel Potter
