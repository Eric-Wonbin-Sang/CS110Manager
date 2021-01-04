# I, Michael Catania, agree to the Stevens Honor Code
# This code determines if you have a healthy BMI
def main():
    print("This program determines if your BMI is healthy.")
    w = float(input("Enter your weight in pounds:"))
    h = float(input("Enter your height in inches:"))
    bmi = (w*720)/(h ** 2)
    if bmi < 19:
        print("\nYour BMI is below the healthy range")
    elif bmi > 25:
        print("\nYour BMI is above the healthy range")
    else:
        print("\nYour BMI is within the healthy range")
main()
    
