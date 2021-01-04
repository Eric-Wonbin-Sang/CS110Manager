#hw6 problem 2
#I pledge my honor that I have abided by the Stevens honor system -Maya O

def main():
    weight = int(input("Please enter your weight in pounds: "))
    height = int(input("Please enter your height in inches: "))
    bmi = (720 * weight)/(height ** 2)
    print()

    if bmi <19:
        print("Based on your height and weight, your BMI is below the healthy range")

    elif bmi >=19 and bmi <= 25:
        print("Based on your height and weight, your BMI is within the healthy range")

    elif bmi >25:
        print("Based on your height and weight, your BMI is above the healthy range")
main()
