# Problem 1
# I pledge my honot that I have abided by the Stevens Honor System
def main():
    weight = int(input("Enter your weight in pounds: "))
    height = int(input("Enter your height in inches: "))
    bmi = weight*720 / height**2 
    print("Your BMI is", bmi)
    if bmi >= 26:
        print("Your BMI is above the healthy range")
    if bmi <= 18:
        print("Your BMI is below the healthy range")
    else: 
        print("Your BMI is within the healthy range")
main()
