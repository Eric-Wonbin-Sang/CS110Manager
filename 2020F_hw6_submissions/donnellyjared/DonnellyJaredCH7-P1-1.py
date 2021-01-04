# I pledge my Honor that I have abided by the Stevens Honor System

def bmi_calculator():
    user_weight = float(input("What is your weight in pounds? "))
    user_height = float(input("What is your height in inches? "))
    bmi = (user_weight * 720) / (user_height ** 2)
    print("Your BMI is: ", round(bmi, 2))

    if bmi > 25:
        print("Your BMI is above the healthy range.")
    elif bmi < 19:
        print("Your BMI is below the healthy range.")
    else:
        print("Your BMI is within the healthy range.")


bmi_calculator()
