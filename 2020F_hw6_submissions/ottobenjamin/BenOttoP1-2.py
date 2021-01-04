#I pledge my honor that I have abided by the Stevens Honor System
#Ben Otto

#This program calculates a person's BMI (Body Mass Index)

def main():
    height=input("Enter your height in the format feet, inches(ex. 5,10)").split(",")
    heightin=float(height[0])*12 + float(height[1])
    weight=float(input("Please enter your weight"))
    bmi=weight*720/(heightin**2)
    if (bmi>25):
        print("Your BMI is above the healthy range.")
    elif(bmi<19):
        print("Your BMI is below the healthy range.")
    else:
        print("Your BMI is within the healthy range.")

main()