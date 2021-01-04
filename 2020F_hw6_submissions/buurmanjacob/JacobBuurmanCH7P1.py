#HW7P1
#By: Jacob Buurman
#I pledge my honor that I have abided by the Stevens Honor System.


# This program will prompt the user to enter their weight in pounds and height
# in inches, calculate their BMI, and say if they are below, within, or above
# the healthy range of 19-25.
def main():
    weight = eval(input("What is your weight (in pounds)?: "))
    height = eval(input("What is your height (in inches)?: "))
    bmi = (720 * weight) / (height ** 2)
    print("Your BMI is", bmi)
    if bmi > 25:
        print("You are ABOVE the healthy BMI range.")
    if bmi < 19:
        print("You are BELOW the healthy BMI range.")
    if 19 <= bmi <= 25:
        print("You are WITHIN the healthy BMI range. :-)")
main()