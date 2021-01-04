#i pledge my honor that I have abided by the stevens honor system- rachel flynn
def main():
    weight= float(input("Enter your weight in pounds: "))
    height= float(input("Enter your height in inches: "))
    bmi = (weight*720)/(height*height)
    if (bmi < 19):
        print("Below Healthy Range")
    elif (bmi == 19 or bmi <= 25):
        print("Within Healthy Range")
    else:
        print("Above Healthy Range")

main()
