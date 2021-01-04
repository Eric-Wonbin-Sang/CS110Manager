#Kayla Batzer HW 6 P1
#I pledge my honor to abide by the Stevens honor code

def main():

    weight = int(input("Enter your weight in pounds: "))
    height = int(input("Enter your height in inches: "))
    BMI = (weight * 720) / (height ** 2)

    if 19 <= BMI <= 25:
        print("This person's BMI is within the healthy range.")

    if BMI > 25:
        print("This person's BMI is above the healthy range.")

    if BMI < 19:
        print("This person's BMI is below the healthy range.")

main()