# i pledge my honor i have abided by the stevens honor system

def main():
    print("This program will calculate your BMI and it will determine if it is under, above or at the healthy level.")
    weight = float(input("Enter weight in pounds: "))
    height = float(input("Enter heihgt in inches: "))
    bmi = 720*weight / height**2
    print(bmi)

    if bmi >= 19 and bmi <= 25:
        print("You have a healthy BMI")

    elif bmi < 19:
        print("You are below a healthy BMI")

    else:
        print("You are above a healthy BMI")

main()
