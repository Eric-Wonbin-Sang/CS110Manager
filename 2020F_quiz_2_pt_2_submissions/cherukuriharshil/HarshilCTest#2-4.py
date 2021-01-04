# Pledge: I pledge my Honor that I abide by the Stevens Honor System
# I understand that I may access the course textbook and course lecture notes
# but I am not to access any other resource. I also pledge that I worked alone on this exam.
# Harshil Cherukuri

def Addition():

    print("This program performs addition of two numbers")
    addition_1 = int(input("What is your first number? "))
    addition_2 = int(input("What is your second number? "))

    result_1 = addition_1 + addition_2
    print("This is your final result", result_1)

def Subtraction():

    print("This program performs subtraction of two numbers")
    subtraction_1 = int(input("What is your first number? "))
    subtraction_2 = int(input("What is your second number? "))

    result_2 = subtraction_1 - subtraction_2
    print("This is your final result", result_2)

def Multiplication():

    print("This program performs multiplication of two numbers")
    multiplication_1 = int(input("What is your first number input? "))
    multiplication_2 = int(input("What is your second number? "))

    result_3 = multiplication_1 * multiplication_2
    print("This is your final result", result_3)

def Division():

    print("This program performs division of two numbers")
    division_1 = int(input("What is your first number? "))
    division_2 = int(input("What is your second number? "))

    result_4 = division_1 - division_2
    print("This is your final result", result_4)

def Vowels():

    input_string = input("Please enter your string: ")
    input_lowercase = input_string.lower()

    vowels_count = {}

    for vowel in "aeiou":
        count = input_lowercase.count(vowel)
        vowels_count[vowel] = count

    counts = vowels_count.values()
    total_vowels = sum(counts)
    print("There are", total_vowels, "vowels in your string input")

def Encryption(): # substitution cipher
    message = input("Enter message to encode: ")
    print("\nHere is the encrypted message: ")

    for i in message:
        x = ord(i)
        print(" ", x + 5, end="")
    print()


def main():
    print("Do you want the program to perform Mathematical Functions?")
    print("If so, please enter the number 1")
    print("Do you want the program to perform String Operations?")
    print("If so, please enter the number 2")

    base_input = int(input("What number do you want the program to perform? "))

    if base_input == 1:
        print()
        print("Do you want the program to perform Addition?")
        print("If so, please enter the number 1")
        print()
        print("Do you want the program to perform Subtraction?")
        print("If so, please enter the number 2")
        print()
        print("Do you want the program to perform Multiplication?")
        print("If so, please enter the number 3")
        print()
        print("Do you want the program to perform Division?")
        print("If so, please enter the number 4")
        print()
        input_1 = int(input("What number do you want the program to perform? "))

        if input_1 == 1:
            Addition()
        elif input_1 == 2:
            Subtraction()
        elif input_1 == 3:
            Multiplication()
        elif input_1 == 4:
            Division()

    elif base_input == 2:
        print()
        print("Do you want the program to determine the number")
        print("of vowels in your input string?")
        print("If so, please enter the number 1")
        print()
        print("Do you want the program to perform Encryption?")
        print("If so, please enter the number 2")
        print()
        input_2 = int(input("What number do you want the program to perform? "))

        if input_2 == 1:
            Vowels()
        elif input_2 == 2:
            Encryption()

    else:

        print("This is not a valid number input")
        print("Please re-run and enter a valid input")


main()