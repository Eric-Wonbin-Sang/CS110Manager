def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def vowels(string):
    vowel = "aeiou"
    string = string.lower()
    count = 0

    for x in string:
        if x in vowel:
            count = count+1

    return count

def encrypt(string):
    return string[::-1]

menu = input("For Mathematical functions, Please Enter the Number 1 " + "\n"
            + "For String Operations, Please Enter the Number 2 \n")

if menu == '1':
    menu = input("For Addition, Please Enter the Number 1 \n" + "For subtraction, Please Enter the Number 2 \n" + "For Multiplication, Please Enter the Number 3 \n" + "For Division, Please Enter the Number 4 \n")
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    if menu == '1':
        print(add(num1, num2))
    elif menu == '2':
        print(subtract(num1, num2))
    elif menu == '3':
        print(multiply(num1, num2))
    elif menu == '4':
        print(divide(num1, num2))
    else:
        print("Invalid Menu Number!")

elif menu == '2':
    menu = input("To Determine the Number of Vowels in a String; Enter the Number 1 \n" + "To Encrypt a String; Enter Number 2 \n")
    string = input("Enter a String: ")

    if menu == '1':
        print(vowels(string))
    elif menu == '2':
        print(encrypt(string))
    else:
        print("Invalid Menu Number")
else:
    print("Invalid Menu Number")