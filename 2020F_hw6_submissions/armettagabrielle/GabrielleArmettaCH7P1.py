# I pledge my honor that I have abided by the Stevens Honor Code
# Gabrielle Armetta

# A program which calculates a person’s BMI and prints a message
# stating whether the person is above, within, or below the healthy range

def main():
    height = int(input("Enter the height in inches:"))
    weight = int(input("Enter the weight in pounds: "))
    BMI = (weight * 720)/ (height**2)
    if BMI < 19:
        print("Under healthy range")
    elif BMI > 25:
        print("Above healthy range")
    else:
        print("Within healthy range")
main()