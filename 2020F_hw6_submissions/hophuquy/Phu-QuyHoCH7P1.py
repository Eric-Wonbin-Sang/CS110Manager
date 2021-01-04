# I pledge my honor that I have abided by the Stevens Honor System
# Problem One
import math

weight = int(input("What is your weight in pounds?"))
height = int(input("What is your height in inches?"))

BMI = (weight*720)/(height ** 2)
print(BMI)
if BMI > 25:
    print("Your BMI is above the healty range.")
elif BMI < 19:
    print("Your BMI is below the healty range.")
else:
    print("Your BMI is within the healty range.")
