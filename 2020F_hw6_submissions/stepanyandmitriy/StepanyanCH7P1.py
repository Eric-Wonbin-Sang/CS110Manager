#StepanyanCH7P1.py
#I pledge my honor that I have abided by the Stevens Honor System
#This program calculates a person's BMI
#and determines the healthiness of the BMI

def main():
    Weight = float(input("Input weight in lbs: "))
    Height = float(input("Input height in inches: "))

    BMI = Weight*720/(Height*Height)

    if 19 > BMI:
        a = "BMI is below the healthy range."

    elif 19 <= BMI <= 25:
        a = "BMI is within the healthy range."

    else:
        a = "BMI is above the healthy range."

    print("The BMI is ", BMI,".","\n", a, sep="")
main()
