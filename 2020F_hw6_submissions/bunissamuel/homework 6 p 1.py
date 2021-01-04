def main():
    print("This program calculates your BMI and tells you if it's healthy or not")
    healthy = range(19, 26)
    x = float(input("Enter your weight in pounds: "))
    y = float(input("Enter your height in inches: "))
    bmi = (x * 720) / (y ** 2)
    if bmi < 19 or bmi > 25:
        print("your bmi is", bmi, "which is unhealthy")
    else:
        print("your bmi is", bmi, "which is healthy")


main()
