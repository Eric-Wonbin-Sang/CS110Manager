#I pledge my honor that I have abided by the Stevens Honor System. Jake Roux
def main():
    weight = eval(input("What is your weight in lbs?:"))
    height = eval(input("What is your height in inches?:"))

    bmi = (weight*720)/(height**2)

    print("Your Body Mass Index is",bmi,", ")

    if bmi < 19:
        print("which is below the healthy range")

    if bmi > 25:
        print("which is above the healthy range")

    if 19 <= bmi <= 25:
        print("which is within the healthy range")

main()
