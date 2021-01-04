# I pledge my honor that I have abided by the Stevens Honor Code
# Riley Sikorski

def main():
    weight = eval(input("Please enter your weight in pounds:"))
    height = eval(input("Please enter your height in inches:"))
    index = (weight * 720) / (height * height)
    print("Your BMI is ", index)
    if 19 <= index <= 25:
        print("Your BMI is within the healthy range! Nice!")
    if index < 19:
        print("Your BMI is below the healthy range.")
    if index > 25:
        print("Your BMI is above the healthy range.")
main()
