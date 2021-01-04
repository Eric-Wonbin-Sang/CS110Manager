#function to analyze BMI levels
def main():
    weight = float(input("Enter weight (in pounds): "))
    height = float(input("Enter height (in inches): "))
    BMI = weight * 720 / ((height) ** 2)

    if BMI < 19:
        print("You are below the healthy range and have a BMI of", BMI)
    elif BMI >= 19 and BMI <= 25:
        print("You are within the healthy range and have a BMI of", BMI)
    elif BMI > 25:
        print("You are above the healthy range and have a BMI of", BMI)

    else:
        print("Recheck the input values correctly and try again")
main()

