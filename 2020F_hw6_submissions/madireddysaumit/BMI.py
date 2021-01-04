#Saumit Madireddy

#I pledge my honor that I have abided by the Stevens Honor System.


def main():
    print("This program will determine your BMI and whether or not it is healthy.")
    w = eval(input("How much do you weigh (lbs) ?  "))
    h = eval(input("How tall (inches) are you? "))
    BMI = (w * 720) / (h * h)
    print("Your BMI is", BMI)
    if BMI <= 25 and BMI >= 19:
        print("Your BMI is healthy")
    else:
        print("Your BMI is not healthy")
    
main()
