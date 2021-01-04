def main():
    print("This program will calculate your BMI and tell whether it's above, below, or within the healthy range.")
    weight = int(input("What is your weight in pounds?"))
    height = int(input("What is your height?"))
    finalheight = height ** 2
    bmi = (weight * 720) / finalheight
    finalbmi = str(bmi)
    if bmi < 19:
        finalbmi = "below"
    if bmi >= 19 and bmi <= 25:
        finalbmi = "within"
    if bmi > 25:
        finalbmi = "over"
    print("Your bmi is", finalbmi, "the healthy range.")


main()
