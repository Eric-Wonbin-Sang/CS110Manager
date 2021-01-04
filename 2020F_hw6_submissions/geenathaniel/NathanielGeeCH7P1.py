#I pledge my honor that I have abided by the Stevens Honor System. Nathaniel Gee

weight=float(input("Enter your weight in pounds: "))
height= float(input("Enter your height in inches: "))

BMI= (weight*720)/(height**2)

if 19<= BMI <= 25:
    print("Your BMI is considered healthy")
else:
    print("Your BMI is NOT considered healthy")




