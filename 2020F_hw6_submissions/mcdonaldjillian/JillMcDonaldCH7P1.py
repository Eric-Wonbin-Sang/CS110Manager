#I pledge my honor that I have abided by the Stevens Honor System. Jill McDonald
#Problem 1

def bmi(weight, height):
    bmi = weight * 720 / height ** 2

    print('Your BMI is', bmi)

    if bmi < 19:
        print('Your BMI is considered below the healthy range.')
    elif bmi <= 25:
        print('Your BMI is considered within the healthy range.')
    else:
        print('Your BMI is considered above the healthy range.')


weight = float(input('How much do you weigh: '))
height = float(input('How tall are you in inches: '))
bmi(weight, height)
    
