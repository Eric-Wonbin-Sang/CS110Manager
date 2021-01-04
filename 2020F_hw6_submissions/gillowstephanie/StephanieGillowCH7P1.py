# Stephanie Gillow
# CS110
# I pledge my honor I have abided by the Stevens honor system.

h = input("Enter your height in inches: ")
w = input("Enter your weight in pounds: ")

bmi = (int(w)*720)/(int(h)*int(h))
if bmi > 26:
    print("Your BMI is above the healthy range.")
elif bmi < 19:
    print("Your BMI is below the healthy range.")
else:
    print("Your BMI is within the healthy range.")
