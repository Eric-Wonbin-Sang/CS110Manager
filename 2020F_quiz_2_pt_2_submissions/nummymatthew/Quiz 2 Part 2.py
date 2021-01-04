#################################################################################
# Name       : Matthew Nummy
# Date       : 11/25/2020
# Assignment : Quiz 2 - Part 2
# Pledge     : I pledge my Honor that I have abided by the Stevens Honor System
#              I understand that I may access the course textbook and course lecture notes but I am not to access any
#              other resource. I also pledge that I worked alone on this exam.
#################################################################################


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


# Finds and returns the number of vowels in the provided string.
def vowel_finder(string):
    i = 0
    vowels = set("aeiouAEIOU")
    for alphabet in string:
        if alphabet in vowels:
            i += 1
    return i


# Creates an array where each index contains a letter from the string. Spaces are removed.
def split_string(string):
    string_array = [char for char in string]
    remove = [' ']
    return [i for i in string_array if i not in remove]


# This function creates the string encryption.
def string_encryption(string):
    letter_array = split_string(string)
    word_array = string.split(' ')
    space_array = [0] * len(word_array)

    # letter_dict assigns each letter in the alphabet a numerical key 1-26. The keys are assigned based on the
    # frequency with which the letters appear in the english language.
    letter_dict = dict({1: ['E', 'e'],
                        2: ['T', 't'],
                        3: ['A', 'a'],
                        4: ['O', 'o'],
                        5: ['I', 'i'],
                        6: ['N', 'n'],
                        7: ['S', 's'],
                        8: ['H', 'h'],
                        9: ['R', 'r'],
                        10: ['D', 'd'],
                        11: ['L', 'l'],
                        12: ['C', 'c'],
                        13: ['U', 'u'],
                        14: ['M', 'm'],
                        15: ['W', 'w'],
                        16: ['F', 'f'],
                        17: ['G', 'g'],
                        18: ['Y', 'y'],
                        19: ['P', 'p'],
                        20: ['B', 'b'],
                        21: ['V', 'v'],
                        22: ['K', 'k'],
                        23: ['J', 'j'],
                        24: ['X', 'x'],
                        25: ['Q', 'q'],
                        26: ['Z', 'z']})

    # This dictionary will be used to represent the length of the preceding word as [a] letter(s). Max word length of
    # 52 characters (represented as ZZ).
    spaces_dict = dict({1: 'A',
                        2: 'B',
                        3: 'C',
                        4: 'D',
                        5: 'E',
                        6: 'F',
                        7: 'G',
                        8: 'H',
                        9: 'I',
                        10: 'J',
                        11: 'K',
                        12: 'L',
                        13: 'M',
                        14: 'N',
                        15: 'O',
                        16: 'P',
                        17: 'Q',
                        18: 'R',
                        19: 'S',
                        20: 'T',
                        21: 'U',
                        22: 'V',
                        23: 'W',
                        24: 'X',
                        25: 'Y',
                        26: 'Z'})

    # Replaces letters in letter_array with corresponding numerical keys.
    for i in range(len(letter_array)):
        for j in range(1, 27):
            if letter_array[i] in letter_dict[j]:
                letter_array[i] = j

    # Creates array of letters that represent word lengths.
    for i in range(len(word_array)):
        if len(word_array[i]) < 27:
            space_array[i] = spaces_dict[len(word_array[i])]
        elif 26 < len(word_array[i]) < 53:
            remainder = len(word_array[i]) - 26
            space_array[i] = 'Z' + spaces_dict[remainder]
        else:
            return "Error"

    return string_builder(word_array, letter_array, space_array)


# This function builds the string that is printed to the console.
def string_builder(word_array, letter_array, space_array):
    encrypted_string_array = [0] * len(letter_array)
    encrypted_string = ""
    pop_list = []
    word_lengths = []

    # Fills array with encrypted letters
    for i in range(len(letter_array)):
        encrypted_string_array[i] = letter_array[i]

    # Places "word-length letters" after each word.
    for i in range(len(word_array)):
        gap_between_spaces = sum(word_lengths) + i + len(word_array[i])
        encrypted_string_array.insert(gap_between_spaces, space_array[i])
        word_lengths.append(len(word_array[i]))

    # Removes extra 0s from encrypted_string_array and turns the array into a string.
    for i in range(len(encrypted_string_array)):
        if encrypted_string_array[i] == 0:
            pop_list.append(i)
        else:
            encrypted_string += str(encrypted_string_array[i])
    for i in reversed(pop_list):
        encrypted_string_array.pop(i)
    return encrypted_string


def main():
    # Parsing user input.
    print("For Mathematical Functions, Please Enter the Number 1")
    print("For String Operations, Please Enter the Number 2")
    main_menu_choice = raw_input("Your choice: ")
    if not unicode(main_menu_choice).isnumeric():
        print("Invalid input. 1 or 2 expected.")
        return 0
    main_menu_choice = int(main_menu_choice)
    if main_menu_choice == 1:
        print("For Addition, Please Enter the Number 1")
        print("For Subtraction, Please Enter the Number 2")
        print("For Multiplication, Please Enter the Number 3")
        print("For Division, Please Enter the Number 4")
        math_func_choice = raw_input("Your choice: ")
        if not unicode(math_func_choice).isnumeric():
            print("Invalid input. 1, 2, 3 or 4 expected.")
            return 0
        math_func_choice = int(math_func_choice)
        if math_func_choice == 1:
            x = int(input("Enter your first operand: "))
            y = int(input("Enter your second operand: "))
            result = addition(x, y)
            print("The sum of " + str(x) + " and " + str(y) + " is " + str(result) + ".")
        elif math_func_choice == 2:
            x = int(input("Enter your first operand: "))
            y = int(input("Enter your second operand: "))
            result = subtraction(x, y)
            print("The difference between " + str(x) + " and " + str(y) + " is " + str(result) + ".")
        elif math_func_choice == 3:
            x = int(input("Enter your first operand: "))
            y = int(input("Enter your second operand: "))
            result = multiplication(x, y)
            print("The product of " + str(x) + " and " + str(y) + " is " + str(result) + ".")
        elif math_func_choice == 4:
            x = int(input("Enter your first operand: "))
            y = int(input("Enter your second operand: "))
            result = division(x, y)
            print("The quotient of " + str(x) + " divided by " + str(y) + " is " + str(result) + ".")
        else:
            print("Invalid input. 1, 2, 3 or 4 expected.")
    elif main_menu_choice == 2:
        print("To Determine the Number of Vowels in a String; Enter the Number 1")
        print("To Encrypt a String; Enter the Number 2")
        string_operation_choice = raw_input("Your choice: ")
        string = raw_input("Enter your string: ")
        if not unicode(string_operation_choice).isnumeric():
            print("Invalid input (string operation choice). 1 or 2 expected. 1")
            return 0
        string_operation_choice = int(string_operation_choice)
        if string != '' and all(chr.isalpha() or chr.isspace() for chr in string):
            if string_operation_choice == 1:
                print("There are " + str(vowel_finder(string)) + " vowels in the word(s) '" + string + "'.")
            elif string_operation_choice == 2:
                if string_encryption(string) == 'Error':
                    print("Error: String contains a word longer than 52 characters.")
                    return 0
                else:
                    result = string_encryption(string)
                    print("Your encrypted string is: " + result)
            else:
                print("Invalid input (string operation choice). 1 or 2 expected. 2")
        else:
            print("Invalid input (string). Only letters and spaces allowed.")
    else:
        print("Invalid input. 1 or 2 expected.")


main()

