#Philip Brendel
#I pledge my honor that I have followed the Stevens Honor code

def bmiCalc():
    weight = int(input("Please enter your weight (in pounds): "))
    height = int(input("Please enter your height (in inches): "))

    bmi = (weight * 720)/(height**2)

    if bmi < 19:
        print("Your BMI is ", bmi, "which is under what is considered healthy.")

    elif bmi > 25:
        print("Your BMI is ", bmi, "which is over what is considered healthy.")

    else:
         print("Your BMI is ", bmi, "which is in the healthy range.")


bmiCalc()
