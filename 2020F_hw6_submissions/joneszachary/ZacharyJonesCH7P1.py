#I pledge my honor that I have abided by the Stevens Honor System.
#Zachary Jones
#HW6 Problem 1

def get_weight():
    weight = float(input('Input weight in lbs: '))
    return weight


def get_height():
    height = float(input('Input height in inches: '))
    return height


def get_bmi(weight, height):
    bmi = round(weight * 720 / height ** 2, 2)

    if bmi < 19:
        print('Below healthy BMI range: {}'.format(bmi))
    elif bmi > 25:
        print('Above healthy BMI range: {}'.format(bmi))
    else:
        print('Within healthy BMI range: {}'.format(bmi))


get_bmi(get_weight(), get_height())