#Sidharth Peri
#CS-110-A
#Honor Code: I pledge in my honor that I have abided by the Stevens Honor System

#A program that calculates a person's bmi and outputs whether the person is within, below, or
#above the healthy range

#function that takes in weight and hieght inputs as parameters and calculates and returns bmi
def calculate_bmi(weight, height):
    bmi = ((weight * 720) / (height ** 2))
    return bmi

def main():
    #inputs for weight and height
    person_weight = int(input("Please enter your weight (in pounds): "))
    person_height = int(input("Please enter your height (in inches): "))
    print()

    #call calculate_bmi function and set bmi equal to variable
    person_bmi = calculate_bmi(person_weight, person_height)

    #conditionals to check what range the bmi is in
    if (person_bmi < 19):
        print("You are below the healthy range")
    elif (person_bmi <= 25):
        print("You are in the healthy range")
    else:
        print("You are above the healthy range")

main()
