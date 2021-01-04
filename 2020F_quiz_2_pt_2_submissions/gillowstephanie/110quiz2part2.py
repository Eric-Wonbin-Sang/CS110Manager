# I pledge my Honor that I have abided by the Stevens Honor System
# I understand that I may access the course textbook and course lecture notes but I am not to access
# any other resource. I also pledge that I worked alone on this exam.
# Stephanie Gillow
# CS 110 quiz 2 part 2
# 11/25/2020

# math functions
def add(num1, num2):
    # adds
    return num1 + num2
def subtract(num1, num2):
    # subtracts
    return num1 - num2
def multiply(num1, num2):
    # multiplies
    return num1 * num2
def divide(num1, num2):
    # divides
    return num1/num2

# string functions
def vowelCheck(v):
    # helper for vowelCount, checks if the character passed to it is a vowel
    return v.lower() in ['a', 'e', 'i', 'o', 'u']
def vowelCount(vowel):
    # counts the amount of vowels in a string by comparing each character using vowelCheck
    numVowels = 0
    for i in range(len(vowel)):
        if vowelCheck(vowel[i]):
            numVowels += 1
    return numVowels
def encrypt(eString, eshift):
    encryptedList = []
    tempList = []
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    for char in eString:
        if char in uppercase:
            index = uppercase.index(char)
            cryptTemp = (index + eshift) % 26
            tempList .append(cryptTemp)
            newLetter = uppercase[cryptTemp]
            encryptedList.append(newLetter)
        elif char in lowercase:
            index = lowercase.index(char)
            cryptTemp = (index + eshift) % 26
            tempList .append(cryptTemp)
            newLetter = lowercase[cryptTemp]
            encryptedList.append(newLetter)
        else:
            encryptedList.append(" ")
        finishedString = ""
        for c in encryptedList:
            finishedString += c
    return finishedString




# spaghetti elif time
# main menu
print("For Mathematical Functions, Please Enter the Number 1")
mainInput = input("For String Operations, Please Enter the Number 2")

if int(mainInput) == 1:
    # math menu
    print("For Addition, Please Enter the Number 1")
    print("For Subtraction, Please Enter the Number 2")
    print("For Multiplication, Please Enter the Number 3")
    mathInput = input("For Division, Please Enter the Number 4")
    if int(mathInput) == 1:
        # add menu
        firstNum = int(input("Please enter your first number: "))
        secondNum = int(input("Please enter your second number: "))
        print("The result is: " + str(add(firstNum, secondNum)))
    elif int(mathInput) == 2:
        # subtraction menu
        firstNum = int(input("Please enter your first number: "))
        secondNum = int(input("Please enter your second number: "))
        print("The result is: " + str(subtract(firstNum, secondNum)))
    elif int(mathInput) == 3:
        # multiplication menu
        firstNum = int(input("Please enter your first number: "))
        secondNum = int(input("Please enter your second number: "))
        print("The result is: " + str(multiply(firstNum, secondNum)))
    elif int(mathInput) == 4:
        # division menu
        firstNum = int(input("Please enter your first number: "))
        secondNum = int(input("Please enter your second number: "))
        print("The result is: " + str(divide(firstNum, secondNum)))
    else:
        print("Sorry, that's not a valid input.")
elif int(mainInput) == 2:
    # string menu
    print("To Determine the Number of Vowels in a String; Enter the Number 1")
    stringInput = input("To Encrypt a String; Enter the Number 2")
    if int(stringInput) == 1:
        # vowel check menu
        vowelString = input("Please input your string: ")
        print("Your string has " + str(vowelCount(vowelString)) + " vowels.")
    elif int(stringInput) == 2:
        # encrypt menu
        encryptString = input("Please input your string: ")
        shift = input("Please enter how many steps to shift: ")
        print("Your encrypted string is: " + encrypt(encryptString, int(shift)))
    else:
        print("Sorry, that's not a valid input.")
else:
    print("Sorry, that's not a valid input.")
