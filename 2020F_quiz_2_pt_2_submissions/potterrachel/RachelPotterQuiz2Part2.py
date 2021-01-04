# RachelPotterQuiz2Part2V1.py

def menu():
    print("For mathematical functions, please enter the number 1.")
    print("For string operations, please enter the number 2.")
    menu_select = input("Please enter your number: ")
    return menu_select


def calculator_menu():
    print()
    print("For addition, please enter the number 1.")
    print("For subtraction, please enter the number 2.")
    print("For multiplication, please enter the number 3.")
    print("For division, please enter the number 4.")
    calculator_select = input("Please enter your number: ")
    return calculator_select


def addition():
    print()
    x = float(input("Please enter the first number you would like to add: "))
    y = float(input("Please enter the second number you would like to add: "))
    xysum = x+y
    return xysum


def subtraction():
    print()
    x = float(input("Please enter the number you would like to subtract from: "))
    y = float(input("Please enter the number you would like to be subtracted from the previous number: "))
    xydifference = (x - y)
    return xydifference


def multiplication():
    print()
    x = float(input("Please enter the first number you would like to multiply: "))
    y = float(input("Please enter the second number you would like to multiply: "))
    xyproduct = x*y
    return xyproduct


def division():
    print()
    x = float(input("Please enter the dividend: "))
    y = float(input("Please enter the divisor: "))
    xyquotient = (x/y)
    return xyquotient


def calculator():
    print()
    calculator_selection = calculator_menu()
    if calculator_selection == "1":
        result1 = addition()
        print(result1)
    elif calculator_selection == "2":
        result2 = subtraction()
        print(result2)
    elif calculator_selection == "3":
        result3 = multiplication()
        print(result3)
    elif calculator_selection == "4":
        result4 = division()
        print(result4)
    else:
        print()
        print("You didn't enter a number 1-4.")


def string_operation_menu():
    print("To determine the number of vowels in a string, please enter the number 1.")
    print("To encrypt a string, please enter the number 2.")
    string_operation_menu_select = input("Please enter your number: ")
    return string_operation_menu_select


def count_vowels():
    print()
    string = input("Please enter a string: ")
    count = 0
    for i in string:
        if i == "a" or i == "A" or i == "e" or i == "E" or i == "i" or i == "I" or i == "o" or i == "O" or i == "u" or i == "U":
            count = count + 1
    return count


def encryption():
    message_list = []
    message = ""
    print()
    string = input("Enter a message to encrypt: ")
    for i in string:
        x = ord(i)
        x = ((x**3) - (x*10)) + 5
        message_list.append(x)
    for i in message_list:
        i = str(i)
        message = message + " " + i
    return message


def string_operation():
    print()
    string_selection = string_operation_menu()
    if string_selection == "1":
        output1 = count_vowels()
        print("There are", output1, "vowels in the string.")
    elif string_selection == "2":
        output2 = encryption()
        print("Your encrypted message is", output2)
    else:
        print()
        print("You didn't enter a number 1 or 2.")


def main():
    user_num = menu()
    if user_num == "1":
        calculator()
    elif user_num == "2":
        string_operation()
    else:
        print()
        print("You didn't enter a number 1 or 2.")


main()

# I pledge my Honor that I have abided by the Stevens Honor System.
# I understand that I may access the course textbook and course lecture notes but I am not to access any other resource.
# I also pledge that I worked alone on this exam.
# Rachel Potter
