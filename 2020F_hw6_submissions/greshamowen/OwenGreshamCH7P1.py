# I pledge my honor that I have abided by the Stevens Honor System - Owen Gresham

def calcBMI(weight, height):
    return (weight * 720) / (height ** 2)


def isBMIHealthy(bmi):
    if bmi < 19:
        print("A BMI of {0:0.2f} is below the healthy range.".format(bmi))
    elif bmi > 25:
        print("A BMI of {0:0.2f} is above the healthy range.".format(bmi))
    else:
        print("A BMI of {0:0.2f} is within the healthy range.".format(bmi))


def main():
    print("This program calculates your BMI and states whether it is healthy or not")
    height = float(input("Enter your height in inches: "))
    weight = float(input("Enter your weight in pounds: "))
    bmi = calcBMI(weight, height)
    print("BMI: {0:0.2f}".format(bmi))
    isBMIHealthy(bmi)


main()