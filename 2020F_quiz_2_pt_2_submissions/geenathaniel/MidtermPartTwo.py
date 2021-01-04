# I pledge my Honor that I have abided by the Stevens Honor System - Nathaniel Gee

def add(n1, n2):
    print("The answer is:", n1 + n2)


def subtract(n1, n2):
    print("The answer is:", n1 - n2)


def multiply(n1, n2):
    print("The answer is:", n1 * n2)


def divide(n1, n2):
    print("The answer is:", n1 / n2)


def vowels(input_string):
    vowel_count = 0
    for v in input_string.lower():
        for w in "aeiou":
            if v == w:
                vowel_count += 1
    print("The number of vowels is:", vowel_count)


def encrypt(input_string):
    print("\nHere is the encrypted message:")
    for s in input_string:
        x = ord(s)
        print(" ", x + 8, end="")


def do_math_operations(sub_menu_item):
    valid_math_inputs = False
    while not valid_math_inputs:
        try:
            number1 = float(input("Please enter the first number: "))
            number2 = float(input("Please enter the second number: "))
            if sub_menu_item == 1:
                add(number1, number2)
            elif sub_menu_item == 2:
                subtract(number1, number2)
            elif sub_menu_item == 3:
                multiply(number1, number2)
            elif sub_menu_item == 4:
                divide(number1, number2)
            valid_math_inputs = True
        except ValueError:
            print("Invalid input,please enter numbers only")
            valid_math_inputs = False


def do_string_operations(sub_menu_item):
    user_string = input("Please enter a string: ")
    if sub_menu_item == 1:
        vowels(user_string)
    elif sub_menu_item == 2:
        encrypt(user_string)


valid_inputs = [1, 2]

# Precess Main Menu
valid_selection = False
main_menu = 0
while not valid_selection:
    print("For Mathematical Functions, Please Enter the Number 1")
    print("For String Operations, Please Enter the Number 2")
    try:
        main_menu = int(input("Please make a selection: "))
        for i in valid_inputs:
            if i == main_menu:
                valid_selection = True
        if not valid_selection:
            print("That is not a valid entry. Valid values are: 1 or 2")
            print("Please try again\n")
    except ValueError:
        print("That is not a valid entry. Valid values are: 1 or 2")
        print("Please try again")

if main_menu == 1:
    valid_inputs.append(3)
    valid_inputs.append(4)

# Process Sub Menu
valid_selection = False
sub_menu = 0
while not valid_selection:
    if main_menu == 1:
        print("For Addition, Please Enter the Number 1\n"
              "For Subtraction, Please Enter the Number 2\n"
              "For Multiplication, Please Enter the Number 3\n"
              "For Division, Please Enter the Number 4")
    elif main_menu == 2:
        print("To Determine the Number of Vowels in a String; Enter the Number 1")
        print("To Encrypt a String; Enter the Number 2")
    try:
        sub_menu = int(input("Please make a selection: "))
        for i in valid_inputs:
            if i == sub_menu:
                valid_selection = True
        if not valid_selection:
            if main_menu == 1:
                print("That is not a valid entry. Valid values are: 1, 2, 3 or 4")
            elif main_menu == 2:
                print("That is not a valid entry. Valid values are: 1 or 2")
            print("Please try again\n")
    except ValueError:
        if main_menu == 1:
            print("That is not a valid entry. Valid values are: 1, 2, 3 or 4")
        elif main_menu == 2:
            print("That is not a valid entry. Valid values are: 1 or 2")
        print("Please try again")

if main_menu == 1:
    do_math_operations(sub_menu)
elif main_menu == 2:
    do_string_operations(sub_menu)
