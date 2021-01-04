# I pledge that I have abided by the Stevens Honor System

def main():
    print("This program will calculate your BMI and tell you whether your BMI is healthy, below healthy, or above a healthy BMI")
    height = float(input("Please enter your height in inches"))
    weight = float(input("Please enter your weight in pounds"))
    bmi = (weight * 720)/(height ** 2)
    print("Your Body Mass Index is", bmi)
    if bmi < 19:
        print("Your BMI is below the healthy range")
    if bmi > 25:
        print("Your BMI is above the healthy range")
    if bmi >= 19 and bmi <= 25:
        print("Your BMI is in the healthy range")

main()


    
