# This is Arjun Koshal's Homework 6 Problem 1
# I pledge my honor that I have abided by the Stevens Honor System
# This program will calculate a person's BMI and will print a message
# stating whether the person is above, within, or below the healthy range

def main():
    print("This is a Body Mass Index Calculator")
    height = float(input("Please enter your height in inches: "))
    weight = float(input("Please enter your weight in pounds: "))

    body_mass_index = weight * 720 / height ** 2
    print(f"\nYour Body Mass Index is {body_mass_index:.2f}")
    if body_mass_index < 19:
        print("Your Body Mass Index is below the healthy range")
    elif body_mass_index <= 26:
        print("Your Body Mass Index is within the healthy range")
    else:
        print("Your Body Mass Index is above the healthy range")

main()