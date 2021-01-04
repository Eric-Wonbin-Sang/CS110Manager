#I pledge my honor that I have abided by the Stevens Honor System
def main():
    weight=float(input("What is the person's weight (in pounds)?:"))
    height=float(input("What is the person's height (in inches)?:"))
    BMI=720*weight/height**2
    print("Your BMI is",BMI)
    if BMI>=19 and BMI<=25:
        print("You are in the healthy BMI range!")
    elif BMI<19:
        print("You are below the healthy BMI range")
    else:
        print("You are above the healthy BMI range")
main()