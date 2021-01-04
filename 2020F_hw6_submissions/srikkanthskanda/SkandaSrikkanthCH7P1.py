# BMI Homework
# I pledge my honor that I have abided by the Stevens Honor System

"""
Inputs: The person's weight and height
Process: Calculating BMI
Outputs: Whether or not the person is in a healthy range
"""


def BMI_calculator(weight, height):
    print("This program calculates a person's BMI given their height (in inches) and weight (in pounds)")
    BMI = (weight * 720) / (height * height)
    print("Your BMI: " + str(BMI))
    if 19 <= BMI <= 25:
        print("Your BMI is at a healthy level!")
    elif BMI < 19:
        print("You seem to be underweight for your height and weight")
    elif BMI > 25:
        print("You seem to be overweight for your height and weight")


BMI_calculator(132, 67)


def valid_date_scanner(month, day, year):
    print("This program accepts a date and sees if it is valid")
    month_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
            26, 27, 28, 29, 30, 31]
    if month in month_numbers:
        print("Valid month")

    if day in days:
        print("Valid day")

    if day == 31:
        if month == '2' or '4' or '6' or '9' or '11':
            print("Invalid day for the month")
        elif month == '1' or '3' or '5' or '7' or '8' or '10' or '12':
            print("Valid day")

    if day == 30:
        if month == '2' or '4' or '6' or '9' or '11':
            print("Valid day")
        elif month == '1' or '3' or '5' or '7' or '8' or '10' or '12':
            print("Invalid day for the month")

    if year > 0:
        print("Valid year")
        print()
    else:
        print("Invalid year")
        print()


valid_date_scanner(7, 6, 1956)
valid_date_scanner(9, 31, 2000)
