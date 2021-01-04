#I pledge my honor I have abided by the Stevens Honor System - Tyson Werner

weight = float(input("What is your weight in pounds: "))
height = float(input("What is your height in inches: "))
BMI = (weight * 720)/(height*height)
if BMI < 19:
    print("below healthy BMI range")

elif 19 <= BMI <=25:
    print("within healthy BMI range")

elif BMI > 25:
    print("above healthy BMI range")