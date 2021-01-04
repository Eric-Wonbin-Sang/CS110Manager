# BMI Calculator
# I pleadge my honor that I have abided by the Stevens Honor System.
# Melissa Atmaca

def main():
    usWeight = float(input("Please enter your weight in pounds: "))
    usHeight = float(input("Please enter your height in inches: "))
    bmi = (usWeight * 720) / (usHeight ** 2)

    if bmi >= 19 and bmi <= 25:
        print("Your BMI is", bmi, "\nYou are within the healthy range.")
    elif bmi < 19:
        print("Your BMI is", bmi, "\nYou are below the healthy range.")
    else:
        print("Your BMI is", bmi, "\nYou are above the healthy range.")
main()

