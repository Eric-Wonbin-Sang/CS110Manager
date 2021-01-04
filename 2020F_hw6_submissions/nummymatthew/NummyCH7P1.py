#################################################################################
# Name       : Matthew Nummy
# Date       : 11/19/2020
# Assignment : Homework 6 - Part 1
# Pledge     : I pledge my honor that I have abided by the Stevens Honor System.
#################################################################################

def main():
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    bmi = float((weight*720)/(height*height))
    print("Your body mass index is: " + str(bmi) + ".")
    if bmi < 19:
        print("Your bmi is below the healthy range.")
    elif bmi > 25:
        print("Your bmi is above the healthy range.")
    else:
        print("Your bmi is within the healthy range.")
main()