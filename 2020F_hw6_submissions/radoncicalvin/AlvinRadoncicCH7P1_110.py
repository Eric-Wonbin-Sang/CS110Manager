# AlvinRadoncicCH7P1_110.py
# I abide by the Stevens Honor Code
# This program accepts any user-inputted weight (in lbs) and height (in inches),
# calculates their BMI, and indicates their BMI in relation to the healthy range.

def get_bmi(weight, height):
    bmi = weight * 720 / (height ** 2)
    bmi = round(bmi, 1)
    return bmi

def main():

    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    bmi = get_bmi(weight, height)
    print("\nYour BMI is", bmi)

    if bmi >= 19 and bmi <= 25:
        print("\nYour BMI is in the healthy range.")
    elif bmi < 19:
        print("\nYour BMI is below the healthy range.")
    else:
        print("\nYour BMI is above the healthy range.")

main()