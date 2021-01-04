#BMI Calculator
#HW6q1
#I pledge my honor that I have abided by the Stevens Honor System

def main():
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    BMI = round((weight*720)/height**2, 3)
    if BMI <= 0:
        print("Error in calculating BMI. Weight cannot be negative.")
    elif 0 < BMI < 19:
        print("Your BMI is", BMI, "and is BELOW the healthy range.")
    elif 19 <= BMI <= 25:
        print("Your BMI is", BMI, "and is WITHIN the healthy range.")
    else:
        print("Your BMI is", BMI, "and is ABOVE the healthy range.")
main()
