#I pledge my Honor that I have abided by the Stevens Honor System.
def main():
    height = float(input("Please enter your height in inches."))
    weight = float(input("Please enter your weight in pounds"))
    BMI = (weight*720)/(height*height)
    BMI = round(BMI,1)
    print("Your BMI is: ", BMI)
    if(BMI < 19):
        print("Your BMI is below the healthy range.")
    elif(BMI > 25):
        print("Your BMI is above the healthy range.")
    else:
        print ("Your BMI is withing the healthy range")
main()