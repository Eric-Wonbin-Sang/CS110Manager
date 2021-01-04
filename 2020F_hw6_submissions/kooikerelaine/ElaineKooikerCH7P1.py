#I pledge my Honor I have abided by the Stevens Honor System. Elaine Kooiker


#Problem One; The Body Mass Index (BMI) is calculated as a person’s weight (in pounds) times 720,
#divided by the square of the person’s height (in inches).
#A BMI in the range of 19 to 25 (inclusive) is considered healthy.
#Write a program which calculates a person’s BMI and prints a message stating whether the person is above, within, or below the healthy range.

import math

def get_BMI(weight, height):
    BMI=(weight*720)/(height**2)
    return BMI

def define_BMI(BMI):
    if (19<=BMI<=25):
        statement="You are within a healthy BMI range."
    elif (BMI>25):
        statement="Your BMI is above a healthy range."
    elif(BMI<25):
        statement="Your BMI is below a healthy range."
    return statement


def main():
    weight=float(input("Enter your weight in pounds: "))
    height=float(input("Enter your height in inches: "))
    BMI=get_BMI(weight, height)
    print(define_BMI(BMI))


main()
