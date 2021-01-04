import csv

file = csv.reader(open('DATABASE-Table 1new.csv'))


def main():
    print("Welcome to car bot!")
    print("I will recommend a car or list of cars to you based on what is most important to you.")
    print("Pick which feature is most important to you when buying a car out of the options presented: ")
    print("1 - luxury")
    print("2 - fuel economy")
    print("3 - body type")
    print("4 - drivetrain")
    print("5 - transmission")
    print("6 - money")
    x = int(input("Enter the number of your most important feature: "))
    if x == 1:
        return luxury()
    elif x == 2:
        return fuel()
    elif x == 3:
        return body()
    elif x == 4:
        return drivetrain()
    elif x == 5:
        return transmission()
    elif x == 6:
        return money()
    else:
        print("this option is invalid")


def luxury():
    print("I define luxury cars as any car which costs over 45 thousand dollars!")
    print("These are the cars I recommend considering which match your selections: ")
    for line in file:
        if int(line[5]) > 45000:
            print(line)


def fuel():
    print("This feature will give you the most fuel efficiant car from the data base")
    print("These are the cars I recommend considering which match your selections: ")
    for line in file:
        if float(line[24]) > 50:
            print(line)


def body():
    print("Select your preferred body style: ")
    print("1 - sedan")
    print("2 - station wagon")
    print("3 - convertible")
    print("4 - hatchback")
    print("5 - pickup truck")
    b = int(input("Enter the number which corresponds with your choice of body style: "))
    print("These are the cars I recommend considering which match your selections: ")
    if b == 1:
        for line in file:
            if str(line[7]) == "Sedan":
                print(line)
    elif b == 2:
        for line in file:
            if str(line[7]) == "Wagon":
                print(line)
    elif b == 3:
        for line in file:
            if str(line[7]) == "Convertible":
                print(line)
    elif b == 4:
        for line in file:
            if str(line[7]) == "Hatchback":
                print(line)
    elif b == 5:
        for line in file:
            if str(line[7]) == "Truck":
                print(line)
    else:
        print("This entry isn't valid")


def drivetrain():
    print("This feature will determine what drivetrain you need and will give you a list of vehicle options")
    print("Pick which mostly describes you")
    print("1 - I live where it snows sometimes")
    print("2 - I go heavy off-roading")
    print("3 - I live in a place where it rains sometimes but it barely ever snows so I don't need extra capability")
    print("4 - I like to race")
    d = int(input("Enter the number of the choice which best describes you: "))
    print("These are the cars I recommend considering which match your selections: ")
    if d == 1:
        for line in file:
            if str(line[19]) == "all wheel drive":
                print(line)
    elif d == 2:
        for line in file:
            if str(line[19]) == "four wheel drive":
                print(line)
    elif d == 3:
        for line in file:
            if str(line[19]) == "front wheel drive":
                print(line)
    elif d == 4:
        for line in file:
            if str(line[19]) == "rear wheel drive":
                print(line)
    else:
        print("This option was not valid")


def transmission():
    print("This feature will give you a list of cars sorted by your transmission preferance")
    print("1 - automatic")
    print("2 - I'm a pro and want to shift myself (manual)")
    t = int(input("Enter the number which corresponds with your choice: "))
    print("These are the cars I recommend considering which match your selections: ")
    if t == 1:
        for line in file:
            if str(line[
                       20]) == "8-speed shiftable automatic" or "7-speed automated manual" or "4-speed automatic" or "6-speed automatic" or "6-speed shiftable automatic" or "10-speed shiftable automatic" or "continuously variable-speed automatic":
                print(line)
    elif t == 2:
        for line in file:
            if str(line[20]) == "5-speed manual" or "6-speed manual":
                print(line)
    else:
        print("this option was not valid")


def money():
    print("This feature automatically finds the cheapest cars from the database")
    print("These are the cars I recommend considering which match your selections: ")
    for line in file:
        if int(line[5]) < 25000:
            print(line)


main()
