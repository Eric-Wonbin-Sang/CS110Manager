height=float(input("Enter your height in inches: "))
weight=float(input("Enter your weight in pounds: "))
BMI=(720*weight)/(height**2)
if 19 < BMI < 25:
    print("Your BMI is within the healthy range")
elif BMI > 25:
    print("You have a BMI above the healthy range")
else:
    print("You have a BMI below the healthy range")

