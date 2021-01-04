#Connor Lucas
#NUmber 1
#I pledge y honor that I have abided by the Stevens Honor Code

def main():
    weight = eval(input("Enter your weight (lbs):"))
    height = eval(input("Enter your height in inches:"))
    bmi = weight*720/height**2
    print ("Your BMI is", bmi)
    if bmi > 25:
        print("You are above the healthy range")
    if bmi < 19:
        print("You are below the healthy range")
    if 19 < bmi < 25:
        print("You are within the healthy range")
main()