# I pledge my honor to abide by the Stevens honor system

def main():
    weight = float(input("Enter weight value in pounds: "))
    height = float(input("Enter height value in inches: "))
    bmi = (weight*720) / (height**2)
    print("BMI is", round(bmi, 2))
    if bmi > 25:
        print("This person's BMI is above the healthy range.")
    elif bmi < 19:
        print("This person's BMI is below the healthy range.")
    else:
        print("This person's BMI is within the healthy range.")


main()