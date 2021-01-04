#I pledge my honor I have abided by the Stevens Honor System

#This program will calculate a person’s BMI and print a message
#stating whether the person is above, within, or below the healthy range

import math

def main():
    print("This program will calculate your BMI by asking for your height and weight")
    print("and inform you whether you are within the healthy BMI range, below it, or above it.")
    print("The healthy BMI range is 19-25.")
    weight= float(input("What is your weight in pounds? "))
    BMIweight = weight * 720
    height = float(input("What is your height in inches? "))
    BMIheight = (math.pow(height,2))
    BMI = BMIweight/BMIheight
    if BMI > 25:
        print("Your BMI is", round(BMI,4))
        print("You are above the healthy BMI range.")
    elif BMI < 19:
        print("Your BMI is", round(BMI,4))
        print("You are below the healthy BMI range.")
    else:
        print("Your BMI is", round(BMI,4))
        print("You are within the healthy BMI range.")
main()