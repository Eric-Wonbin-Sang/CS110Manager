# This is Arjun Koshal's Quiz 2 Part 2 Solution
# I pledge my honor that I have abided by the Stevens Honor System
# This program will present the user with a menu of items
# to select. Once the user selects a menu item, the Python
# program will perform the operation. The options include
# Mathematical functions and String operations. Within the
# Mathematical functions, a user may add, subtract, multiply
# or divide. Within the String operations, a user may
# determine the number of vowels in a string or enrypt a string


def main():
    operation = int(input("Please Enter the Number 1 if you would like Mathematical functions \nor enter the Number 2 if you would like String operations: "))
    while operation > 2 or operation < 1:
        print("\nYou have entered a number out of range. Please try again")
        operation = int(input("\nPlease Enter the Number 1 if you would like Mathematical functions \nor enter the Number 2 if you would like String operations: "))
    if operation == 1:
        while True:
            math_function = int(input("\nEnter 1 if you would like to add, \n2 if you would like to subtract, \n3 if you would like to multiply, \nor 4 if you would like to divide: "))
            while math_function > 4 or math_function < 1:
                print("\nYou have entered a number out of range. Please try again")
                math_function = int(input("\nEnter 1 if you would like to add, \n2 if you would like to subtract, \n3 if you would like to multiply, \nor 4 if you would like to divide: "))

            if math_function >= 1 or math_function <= 4:
                num_1 = float(input("\nEnter the first number: "))
                num_2 = float(input("Enter the second number: "))

                if math_function == 1:
                    print(num_1, "+", num_2, "=", num_1 + num_2)
                elif math_function == 2:
                    print(num_1, "-", num_2, "=", num_1 - num_2)
                elif math_function == 3:
                    print(num_1, "*", num_2, "=", num_1 * num_2)
                elif math_function == 4:
                    print(num_1, "/", num_2, "=", num_1 / num_2)
                break
            else:
                print("Invalid Input")
    if operation == 2:
        str_operation = int(input("\nPlease Enter the Number 1 if you want to determine the vowels \nor enter the number 2 if you want to encrypt a string: "))
        while str_operation > 2 or str_operation < 1:
            print("\nYou have entered a number out of range. Please try again")
            str_operation = int(input("\nPlease Enter the Number 1 if you want to determine the vowels \nor enter the number 2 if you want to encrypt a string: "))
        if str_operation == 1:
            while True:
                str_vowel = str(input("\nPlease enter a string: "))
                lowercase = str_vowel.lower()
                num_of_vowels = {}
                for vowel in "aeiouy":
                    num = lowercase.count(vowel)
                    num_of_vowels[vowel] = num
                print(num_of_vowels)
                break
        if str_operation == 2:
            while True:
                def encryption(line, shift):
                    result = ""
                    for i in range(len(line)):
                        character = line[i]
                        if (character.isupper()):
                            result += chr((ord(character) + shift - 65) % 26 + 65)
                        else:
                            result += chr((ord(character) + shift - 97) % 26 + 97)
                    return result
                line = str(input("\nEnter a string: "))
                shift = int(input("Enter the shift as an integer: "))
                    
                print("Text: " + line)
                print("Shift: " + str(shift))
                print("Cipher: " + encryption(line, shift))
                break

main()