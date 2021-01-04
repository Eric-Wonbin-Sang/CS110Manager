def main():
    print("1 = Mathematical functions")
    print("2 = string operations")
    p = int(input("Enter a number 1 or 2: "))
    if p == 1:
        print(math())
    elif p == 2:
        print("1 = count the number of vowels in a string")
        print("2 = encrypt a string")
        s = int(input("Enter a number 1 or 2: "))
        if s == 1:
            strg = input("enter a string: ")
            print(vowels(strg))
        elif s == 2:
            strg = input("enter a string to be encrypted: ")
            print(encryption(strg))
        else:
            print("error the entry is invalid")
    else:
        print("error the entry is invalid")

def math():
    print("1 = addition")
    print("2 = subraction")
    print("3 = multiplication")
    print("4 = division")
    m = int(input("Enter a number, 1, 2, 3, 4: "))
    if m == 1:
        x = float(input("Enter the first number you want to add: "))
        y = float(input("Enter the second number you want to add: "))
        return addition(x, y)
    elif m == 2:
        x = float(input("Enter the first number you want to subtract: "))
        y = float(input("Enter the second number you want to subtract: "))
        return subtraction(x, y)
    elif m == 3:
        x = float(input("Enter the first number you want to multiply: "))
        y = float(input("Enter the second number you want to multiply: "))
        return multiplication(x, y)
    elif m == 4:
        x = float(input("Enter the first number you want to divide: "))
        y = float(input("Enter the second number you want to divide: "))
        return division(x, y)
    else:
        print("error this entry is invalid")

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def vowels(strg):
    letters = 0
    for character in strg:
        if character in "aeiouAEIOU":
            letters = letters + 1
    return letters

def encryption(strg):
    print("Here is the encrypted message: ")
    st = ""
    for i in strg:
        x = ord(i)
        st = st + str(x) + " "
    return st

main()

#I pledge my honor that I have abided by the Stevens Honor System



