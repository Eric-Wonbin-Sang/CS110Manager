#Quiz 2 Part 2
#By: Jacob Buurman
#November 25, 2020

#I pledge my honor that I have abided by the Stevens Honor System - Jacob Buurman
#I understand that I may access the course textbook and course lecture notes but I
#am not to access any other resource. I also pledge that I worked alone on this exam.

def main():
    num_1 = eval(input("Enter 1 for mathematical functions\nEnter 2 for string operations\n"))
    if num_1 == 1:
        num_2 = eval(input("Enter 1 for addition\nEnter 2 for subtraction\nEnter 3 for multiplication\nEnter 4 for division\n"))
        result = 0
        if num_2 == 1:
            a = float(input("Enter first number to add: "))
            b = float(input("Enter second number to add: "))
            result = round(a + b, 4)
        elif num_2 == 2:
            a = float(input("Enter first number to subtract: "))
            b = float(input("Enter second number to subtract: "))
            result = round(a - b, 4)
        elif num_2 == 3:
            a = float(input("Enter first number to multiply: "))
            b = float(input("Enter second number to multiply: "))
            result = round(a * b, 4)
        elif num_2 == 4:
            a = float(input("Enter first number to divide: "))
            b = float(input("Enter second number to divide: "))
            result = round(a / b, 4)
        else:
            print("ERROR - MUST ENTER 1, 2, 3, OR 4")
        print("The answer is", result)
    elif num_1 == 2:
        num_3 = eval(input("Enter 1 to determine the number of vowels in a string\nEnter 2 to encrypt a string\n"))
        vowels = 0
        if num_3 == 1:
            str = input("Enter a string of characters to see how many vowels there are: ")
            for i in str:
                if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
                    vowels = vowels + 1
            print("There are", vowels, "vowels.")
        elif num_3 == 2:
            str = input("Enter a string of characters to encrypt: ")
            for i in str:
                print("", (ord(i)) ** 3 * 2, end = "")
            print()
        else:
            print("ERROR - MUST ENTER 1 OR 2")
    else:
        print("ERROR - MUST ENTER 1 OR 2")
main()