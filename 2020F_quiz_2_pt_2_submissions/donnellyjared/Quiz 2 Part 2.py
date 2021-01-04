# I pledge my Honor that I have abided by the Stevens Honor System
from math import sqrt
global response_3


def intro():
    try:
        print("\nThis program will allow you to perform either mathematical or string operations")
        print("For Mathematical Functions, Please Enter the Number 1")
        print("For String Operations, Please Enter the Number 2\n")
        response_1 = int(input("Please select the operation you would like to perform:\n"))

        if response_1 == 1:
            math_intro()
        elif response_1 == 2:
            string_intro()
        else:
            print("Your response was invalid, please select an option 1 or 2")
            intro()


        print("\nIf you would like to go again input 1")
        print("If you are finished input 2")
        response_3 = int(input("Would you like to go again??\n"))

        if response_3 == 1:
            intro()
        elif response_3 == 2:
            exit()
        else:
            print("Your input wasn't valid, so we will have you go again")
            intro()
    except ValueError:
        print("\nYour input was invalid, please use options 1 or 2")
        intro()


def math_intro():
    try:
        print("\nFor Addition, Please Enter the Number 1")
        print("For Subtraction, Please Enter the Number 2")
        print("For Multiplication, Please Enter the Number 3")
        print("For Division, Please Enter the Number 4")
        response_2 = int(input(""))

        if response_2 == 1:
            x, y = numbers()
            z = x + y
            print("The sum of", x, "and", y, "is", z)
        elif response_2 == 2:
            x, y = numbers()
            z = x - y
            print("The difference of", x, "and", y, "is", z)
        elif response_2 == 3:
            x, y = numbers()
            z = x * y
            print("The product of", x, "and", y, "is", z)
        elif response_2 == 4:
            x, y = numbers()
            if y != 0:
                z = x / y
                print("The quotient of", x, "and", y, "is", z)
            elif y == 0:
                print("You cannot divide by 0, please reselect your desired math operation and your numbers again")
                math_intro()

        else:
            print("Your response was proper type, but did not select a operation, please selection an option 1 - 4")
            math_intro()

    except ValueError:
        print("Please input a valid response")
        math_intro()


def numbers():
    try:
        x = float(input("\nPlease input your first number: "))
        y = float(input("Please input your second number: "))
        print("")

        return x, y

    except ValueError:
        print("The inputs you provided are invalid for this operation, please provide proper inputs")
        numbers()


def string_intro():
    try:
        print("\nTo Determine the Number of Vowels in a String; Enter the Number 1")
        print("To Encrypt a String; Enter the Number 2")
        response_2 = int(input(""))

        if response_2 == 1:
            vowel_count()
        elif response_2 == 2:
            encryption()
        else:
            print("Please input a valid response")
            string_intro()

    except ValueError:
        print("Please input a valid response")
        string_intro()


def vowel_count():
    string = str(input("\nPlease input your string below: \n"))
    vowel_counter = 0
    y_counter = 0
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for i in string:
        if i in vowel:
            vowel_counter += 1
        elif i == "y":
            y_counter += 1
        elif i == "Y":
            y_counter += 1
    print("\nThe string has", vowel_counter, "vowels in it.")

    if y_counter != 0:
        print("Sometimes y is considered a vowel, and your string has", y_counter, "y's in it.")


def encryption():
    string = str(input("\nPlease input your string below: \n"))
    encryptiod = string.split(" ")
    encryptiod = encryptiod[-1]
    encryptiod_num = []
    string_num = []

    for i in encryptiod:
        encryptiod_num.append(ord(i))

    encryptiod_num = (sum(encryptiod_num) / len(encryptiod_num))
    encryptiod_num = round(sqrt(encryptiod_num))

    for i in string:
        string_num.append(ord(i))

    for i in range(len(string_num)):
        string_num[i] = string_num[i] + encryptiod_num
        string_num[i] = chr(string_num[i])

    print("\nYour encrypted message is:")
    print(''.join(['%-2s' % (i,) for i in string_num]))


intro()
