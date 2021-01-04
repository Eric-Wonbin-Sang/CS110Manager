# Alvin Radoncic
# CS-110-A
# Quiz Two Part Two
# I pledge my Honor that I have abided by the Stevens Honor System

def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def vowels(z):
    lowercased = z.lower()
    num_of_vowels = lowercased.count("a") + lowercased.count("e") + lowercased.count("i") + lowercased.count("o") + lowercased.count("u")
    return num_of_vowels


def encryption(z):
    print("\nHere is your encrypted message: ")
    for i in z:
        x = ord(i)
        print("", x ** 2 / 2, end="")



def main():
    Main_Menu = float(input("For Mathematical Functions, Please Enter the Number 1\nFor String Operations, Please Enter the Number 2\n"))

    if Main_Menu == 1:
        Math_Menu = float(input("\nFor Addition, Please Enter the Number 1\nFor Subtraction, Please Enter the Number 2\nFor Multiplication, Please Enter the Number 3\nFor Division, Please Enter the Number 4\n"))

        if Math_Menu == 1:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(addition(num1, num2))

        elif Math_Menu == 2:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(subtraction(num1, num2))

        elif Math_Menu == 3:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(multiplication(num1, num2))

        elif Math_Menu == 4:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(division(num1, num2))

        else:
            print("\nError: Please input one of the given options.")


    elif Main_Menu == 2:
        String_Menu = float(input("\nTo Determine the Number of Vowels in a String; Enter the Number 1\nTo Encrypt a String; Enter the Number 2\n"))

        if String_Menu == 1:
            string = input("Enter a string: ")
            print()
            print(vowels(string))


        elif String_Menu == 2:
            string = input("Enter a string: ")
            print()
            encryption(string)

        else:
            print("\nError: Please input one of the given options.")

    else:
        print("\nError: Please input one of the given options.")



main()



