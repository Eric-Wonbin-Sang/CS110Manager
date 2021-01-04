# Cahir Geraghty 11/25/20
import math

def addition(x, y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y

def vowels(x):
    final = [each for each in x if each in "aeiou"]
    return len(final)

def encode(x):
    temp =""
    for z in x:
        temp += chr(ord(z)+5)
    return temp



def main():
    i = int(input("For Mathematical Functions, Please Enter the Number 1 \nFor String Operations, Please Enter the Number 2 \n"))
    if i == 1:
        t = int(input("For Addition, Please Enter the Number 1 \nFor Subtraction, Please Enter the Number 2 \nFor Multiplication, Please Enter the Number 3 \nFor Division, Please Enter the Number 4 \n"))
        if t ==1:
            x = float(input("First: "))
            y = float(input("Second: "))
            print(addition(x,y))
        elif t==2:
            x = float(input("First: "))
            y = float(input("Second: "))
            print(subtraction(x, y))
        elif t ==3:
            x = float(input("First: "))
            y = float(input("Second: "))
            print(multiplication(x, y))
        elif t==4:
            x = float(input("First: "))
            y = float(input("Second: "))
            print(division(x, y))
        else:
            print("Not an option")

    elif i == 2:
        t = int(input("To Determine the Number of Vowels in a String; Enter the Number 1 \nTo Encrypt a String; Enter the Number 2 \n"))
        if t==1:
            x = input("String: ")
            print(vowels(x))
        elif t==2:
            x = input("String: ")
            print(encode(x))
        else:
            print("Not an option")
    else:
        print("Not an option")

main()