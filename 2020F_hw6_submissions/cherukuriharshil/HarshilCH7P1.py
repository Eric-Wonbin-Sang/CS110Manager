# Pledge: I pledge my Honor that I  abide by the Stevens Honor System

def bmi():
    print("This is a Body Mass Index Calculator")
    height = int(input("Please enter your height in inches: "))
    weight = int(input("Please enter your weight in lbs: "))

    bmi = (weight * 720)/(height ** 2)

    if bmi < 19:
        print("Your BMI is considered low")
    elif bmi <= 26:
        print("Your BMI is considered healthy")
    else:
        print("Your BMI is considered high")

def main():

    bmi()

main()