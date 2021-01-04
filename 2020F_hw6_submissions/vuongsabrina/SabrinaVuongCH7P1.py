#I pledge on my honor that I have abided by the Stevens Honor System

def main():
    weight = float(input("Please enter your weight in pounds"))
    height = float(input("Please enter your height in inches"))
    bmi = weight*720/(height**2)
    if ((bmi>=19) & (bmi<=25)):
        print("Your bmi is {}, which is in the healthy range".format(bmi))
    else:
        print("Your bmi is {}, which is not in the healthy range.".format(bmi))
 
main()