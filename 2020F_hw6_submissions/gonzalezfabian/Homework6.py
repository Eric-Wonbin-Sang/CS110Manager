#FabianGonzalez

#I pledge my honor that I have abided by the Stevens Honor System. Fabian Gonzalez.

print("")
def BodyMassIndex():
    print('This function will calculate your Body Mass Index (BMI) and determine if it is below, within, or above a healthy range.')
    print("")
    weight = int(input('Enter your weight, in pounds:'))
    print("")
    height = int(input('Enter your height, in inches:'))
    print("")
    BMI = (weight * 720) / (height * height)
    print("Your BMI is:", BMI)
    print("")
    if 19<=BMI<=25:
        print('Your BMI is within a healthy range.')
    if BMI>25:
        print('Your BMI is above the range of healthy weights.')
    if BMI<19:
        print('Your BMI is below the range of healthy weights.')
BodyMassIndex()

print("")

print("This function will determine whether a date is valid or not.")
import datetime
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%m/%d/%Y')
    except ValueError:
        print("")
        print("This date is not valid.")
    else:
        print("")
        print("This date is valid.")
print("")
validate(input("Please enter a date:"))

print("")
input('Press ENTER to exit.')