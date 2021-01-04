#I pledge my honor that I have abided by the Stevens Honor system
#This program will calculate a person's BMI
#It will return if the person is healthy or not
#Using an if elif else statement
def main():
    print("This program will take your wieght and height and calculate your BMI")
    print("It will require you to input your weight rounded to nearest pound")
    print("And your height in inches")

    weight = float(input("Enter your weight to nearest pound: "))
    tall = float(input("Enter your height in inches: "))
                 

    BMI = (weight * 720)/ tall ** 2
    
   

    if BMI >= 19 and BMI <= 25:
                 print("Your BMI:", round(BMI,1), "is healthy!")

    elif BMI < 19:
        print("Your BMI:", round(BMI, 1), "is unhealthy!")

    else:
        print("Your BMI:", round(BMI, 1), "is unhealthy!")

    

main()
    
