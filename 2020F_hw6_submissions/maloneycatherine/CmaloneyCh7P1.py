# Catherine Maloney - CS 110 HW6
# I pledge my honor that I have abided by the Stevens honor system.

# The Body Mass Index (BMI) is calculated as a person's weight (in pounds) times
# 720, divided by the square of the person's height (in inches). A BMI in the
# range of 19 to 25 (inclusive) is considered healthy. Write a program which
# calculates a person's BMI and prints a message stating whether the person is
# above, within, or below the healthy range.

def main():
    
    weight = int(input("Enter your weight in pounds: "))
    height = int(input("Enter your height in inches: "))
    bmi = (weight * 720)/height**2
    print("Your bmi is: ", bmi)

    if bmi > 25:
        print("You are above the healthy bmi range.")
    elif bmi < 19:
        print("You are below the healthy bmi range.")
    else:
        print("You are within the healthy bmi range.")

main()
