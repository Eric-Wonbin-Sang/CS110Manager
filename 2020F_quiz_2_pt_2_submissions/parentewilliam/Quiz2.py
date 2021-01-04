# William Parente
# CS-110: Quiz 2
# I pledge by honor I have abided by the Stevens honor system

def intro():
    print("\nThis program allows you to choose from a variety of operations to perform")
    print("You may choose to perform either mathematical or string operations\n")
    print("If you would like to choose a math operation, input the number 1")
    print("For a string operation, input the number 2\n")


def select():
    try:
        selection = int(input("Enter your input here: "))
        if selection == 1:
            print("\nYou have selected math operations\n")
            op_math()
        elif selection == 2:
            print("You have selected string operations\n")
            op_string()
        else:
            print("\nThe number you entered is invalid, please enter either 1 or 2 to continue\n")
            select()
    except ValueError:
        print("\nYour input was invalid, please enter one of the indicated values to continue\n")
        select()


def op_math_intro():
    print("For addition, please enter the number 1")
    print("For subtraction, please enter the number 2")
    print("For multiplication, please enter the number 3")
    print("For division, please enter the number 4")


def math_add():
    print("Please enter the two values to be added:")
    try:
        factor_1 = float(input("Enter first value: "))
        factor_2 = float(input("Enter the second value: "))
        print("The sum of your values is", factor_1 + factor_2)
    except ValueError:
        print("\nYour input was invalid, please enter numerical values to continue\n")
        math_add()


def math_subtract():
    try:
        print("Please enter two values, the second value will be subtracted from the first:")
        factor_1 = float(input("Enter first value: "))
        factor_2 = float(input("Enter the second value: "))
        print("The difference between your values is", round(factor_1 - factor_2, 2))
    except ValueError:
        print("\nYour input was invalid, please enter numerical values to continue\n")
        math_subtract()


def math_multiply():
    try:
        print("Please enter the two values to be multiplied:")
        factor_1 = float(input("Enter first value: "))
        factor_2 = float(input("Enter the second value: "))
        print("The product of your two values is", round(factor_1 * factor_2, 2))
    except ValueError:
        print("\nYour input was invalid, please enter numerical values to continue\n")
        math_multiply()


def math_divide():
    try:
        print("Please enter two values, the first value will be divided by the second value:")
        factor_1 = float(input("Enter first value: "))
        factor_2 = float(input("Enter the second value: "))
        print("The quotient of your two values is", round(factor_1 / factor_2, 2))
    except ValueError:
        print("\nYour input was invalid, please enter numerical values to continue\n")
        math_divide()


def op_math():
    op_math_intro()
    try:
        selection_math = int(input("\nEnter your selection here: "))
        if selection_math == 1:
            math_add()
        elif selection_math == 2:
            math_subtract()
        elif selection_math == 3:
            math_multiply()
        elif selection_math == 4:
            math_divide()
        else:
            print("The number you entered is invalid, please enter one of the supplied values to continue")
            op_math()
    except ValueError:
        print("\nYour entry is invalid, please enter one of the supplied values\n")
        op_math()


def op_string_intro():
    print("To determine the number of vowels in a string, enter the number 1 "
          "(This program does not consider the special letter 'y' a vowel)")
    print("To encrypt a string, enter the number 2")


def string_vowels():
    try:
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        string = str(input("Enter your string here: "))
        for i in string:
            if i in vowels:
                count += 1
        print("The number of vowels in your string is", count)
    except ValueError:
        print("Your entry was invalid, please enter a string of characters")
        string_vowels()


def string_encrypt():
    code = []
    number = []
    code_encrypt = []
    code_encrypt_letters = []
    new_string = ""
    string = str(input("Enter your string here: "))
    print(string)
    for i in string:            # For each letter in the string, convert it to an ordinal and add it to a new list
        code.append(ord(i))
        number.append(string.count(i))
    for i in range(len(code)):
        if number[i] % 2 == 0:
            code_encrypt.append(code[i] + number[i])
        else:
            code_encrypt.append(code[i] - number[i])        # Program shifts the ordinal value of each character
    for i in range(len(code_encrypt)):                      # by the number of times it appears in the string
        code_encrypt_letters.append(chr(code_encrypt[i]))
    for i in range(len(code_encrypt_letters)):              # Ord value is shifted up if the number of appearances is
        new_string += code_encrypt_letters[i]               # an even number, shifted down if it is odd
    print("Your encrypted string is:", new_string)


def op_string():
    op_string_intro()
    try:
        selection_string = int(input("\nEnter your selection here: "))
        if selection_string == 1:
            string_vowels()
        elif selection_string == 2:
            string_encrypt()
        else:
            print("The number you entered is invalid, please enter one of the supplied values to continue")
            op_string()
    except ValueError:
        print("\nYour entry is invalid, please enter one of the supplied values\n")
        op_string()


intro()
select()
