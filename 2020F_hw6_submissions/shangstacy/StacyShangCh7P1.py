# StacyShangCh7P1.py
# CS 110 A HW 6
# Stacy Shang
# I pledge my honor that I have abided by the Stevens Honor System -Stacy

# This program calculates a person's BMI and prints whether the person is above, within, or below the healthy range.

print("This program will calculate the user's BMI")

def main ():
    bmi_cal()
    
height = 0.0
weight = 0.0
bmi = 0.0

def bmi_cal():
    print()

height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))

bmi = (weight * 703) / (height ** 2)

if bmi < 18.5:
    print("With a BMI of " + str(bmi) + ", the user is below the healthy range.")
elif bmi < 24.9:
    print ("With a BMI of " + str(bmi) + ", the user is within the healthy range.")
else:
    print ("With a BMI of " + str(bmi) + ", the user is above the healthy range.")

main()
