# I pledge my Honor that I have
# abided by the Stevens Honor System.
# Eshita Jain
# program calculated BMI

def main():
    print("This program calculated BMI\n")

    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    print()
    bmi = (weight * 720) / height ** 2

    print("Your BMI is: ", round(bmi))
    print()

    if bmi < 19:
        print("Your BMI is lower than the healthy range.")
    elif bmi <= 25:
        print("Your BMI is healthy.")
    else:
        print("Your BMI is higher than the healthy range.")
main()

