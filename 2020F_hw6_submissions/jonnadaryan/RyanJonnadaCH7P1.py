#Ryan Jonnada
#I pledge that I have abided by the Steven's Honor System

def main():
    weight=eval(input("Enter your weight(lbs):"))
    height=eval(input("Enter your height(inches):"))
    bmi=weight*720/height**2
    print("Your BMI is", bmi)
    if bmi > 25:
        print("You are above the healthy range")
    if bmi < 19:
        print("You are below the healthy range")
    if 19< bmi < 25:
        print("You are within the healthy range")

main()
