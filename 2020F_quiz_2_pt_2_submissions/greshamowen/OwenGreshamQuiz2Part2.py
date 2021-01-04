# I pledge my Honor that I have abided by the Stevens Honor System - Owen Gresham
# Owen Gresham
# 11-25-2020
# CS-110-A
# Quiz 2 Part 2

def is_vowel(letter):
    letter = letter.lower()
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
        return True
    return False


def encrypt(phrase, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    letters = []
    for i in range(len(alphabet)):
        letters.append(alphabet[i])
    encrypted = ""
    for i in phrase:
        if i.lower() == i:
            encrypted += letters[(letters.index(i) + key) % 27]
        elif i.upper() == i:
            encrypted += letters[(letters.index(i.lower()) + key) % 27].upper()
    return encrypted


def add(num1, num2):
    return float(num1) + float(num2)


def subtract(num1, num2):
    return float(num1) - float(num2)


def multiply(num1, num2):
    return float(num1) * float(num2)


def divide(num1, num2):
    return float(num1) / float(num2)


def main():
    print("For Mathematical Functions, Please Enter the Number 1\n"
          "For String Operations, Please Enter the Number 2")
    selection_one = input()

    if selection_one == "1":
        print("For Addition, Please Enter the Number 1\n"
              "For Subtraction, Please Enter the Number 2\n"
              "For Multiplication, Please Enter the Number 3\n"
              "For Division, Please Enter the Number 4")

        selection_two = input()
        if selection_two != "1" and selection_two != "2" and selection_two != "3" and selection_two != "4":
            print("Invalid input")
        else:
            nums = input("Enter two numbers separated by a comma: ").split(",")
            if selection_two == "1":
                try:
                    print(float(nums[0]), "+", float(nums[1]), "=", add(nums[0], nums[1]))
                except (ValueError, IndexError):
                    print("Invalid Input")
            elif selection_two == "2":
                try:
                    print(float(nums[0]), "-", float(nums[1]), "=", subtract(nums[0], nums[1]))
                except (ValueError, IndexError):
                    print("Invalid Input")
            elif selection_two == "3":
                try:
                    print(float(nums[0]), "*", float(nums[1]), "=", multiply(nums[0], nums[1]))
                except (ValueError, IndexError):
                    print("Invalid Input")
            elif selection_two == "4":
                try:
                    print(float(nums[0]), "/", float(nums[1]), "=", divide(nums[0], nums[1]))
                except (ValueError, IndexError):
                    print("Invalid Input")
    elif selection_one == "2":
        print("To Determine the Number of Vowels in a String, Enter the Number 1\n"
              "To Encrypt a String, Enter the Number 2")
        selection_two = input()
        if selection_two != "1" and selection_two != "2":
            print("Invalid input")
        else:
            phrase = input("Please enter a phrase only containing letters and/or spaces: ")
            if selection_two == "1":
                num = 0
                for i in phrase:
                    if is_vowel(i):
                        num += 1
                print("The phrase \"" + phrase + "\" contains", num, "vowels.")
            elif selection_two == "2":
                try:
                    key = int(input("Enter the shift key: "))
                    encrypted = encrypt(phrase, key)
                    print("\nThe encrypted phrase:\n" + encrypted)
                except ValueError:
                    print("Invalid Input")
    else:
        print("Invalid input")

main()
