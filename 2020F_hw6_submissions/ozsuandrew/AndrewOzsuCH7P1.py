def main():
    b=(int(input("Enter your weight in lbs:" )))
    h=(int(input("Enter your height in inches:" )))
    y=(b*720)/h/h
    if 25 >= y >= 19 :
        print ("You are within the healthy range")
    elif y > 25 :
        print ("you are above the healthy range")
    else :
        print ("you are below the healthy range")
           
