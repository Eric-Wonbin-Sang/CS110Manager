#Serena Migdal
#I pledge my honor that I have abided by the stevens honor code

def main():
    print("This program will determine your BMI and evaluate if it is in a healthy range")
    W=eval(input("what is your weight? "))
    H=eval(input("what is your height in inches? "))
    bmi=(W*720)/(H*H)
    print("your BMI is ", bmi)
    if bmi <= 25 and bmi>=19:
        print("your BMI is healthy")
    else:
        print("your bmi is not healthy")
main()

    
