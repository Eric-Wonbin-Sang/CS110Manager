#Kayla Batzer Quiz 2
#I pledge my honor to abide by the Stevens honor code

def addition(x,y):
    add = x + y
    return add

def subtraction(a,b):
    subtract = a - b
    return subtract

def multiplication(c,d):
    multiply = c * d
    return multiply

def division(w,z):
    divide = w / z
    return divide

def vowels(string):
    count = 0
    for letter in string:
        if letter in "aeiouyAEIOUY":
            count = count + 1
    return count

def encryption(string1):
    for i in string1:
        x = ord(i)
        print(" ",x - 7, end="")

def main():
    print("For mathematical functions, please enter the number 1")
    print("For string operations, please enter the number 2")
    menuChoice = int(input("Please enter a number: "))


    if menuChoice == 1:
        print("For addition, please enter the number 1")
        print("For subtraction, please enter the number 2")
        print("For multiplication, please enter the number 3")
        print("For division, please enter the number 4")
        mathChoice = int(input("Please enter a number: "))

        if mathChoice == 1:
            x = float(input("Enter a number to be added: "))
            y = float(input("Enter a number to be added: "))
            answer = addition(x,y)
            print("The sum is:", answer)

        elif mathChoice == 2:
            a = float(input("Enter a number to be subtracted from: "))
            b = float(input("Enter a number to subtract by: "))
            answer2 = subtraction(a,b)
            print("The difference is:", answer2)

        elif mathChoice == 3:
            c = float(input("Enter a number to be multiplied: "))
            d = float(input("Enter a number to be multiplied: "))
            answer3 = multiplication(c,d)
            print("The product is:", answer3)

        elif mathChoice == 4:
            w = float(input("Enter a number to be divided: "))
            z = float(input("Enter a number to divide by: "))
            answer4 = division(w,z)
            print("The quotient is:", answer4)

        else:
            print("The value you have input is invalid.")
            print("Please try again.")

    elif menuChoice == 2:
        print("To determine the number of vowels in a string, please enter the number 1")
        print("To encrypt a string, please enter the number 2")
        stringChoice = int(input("Please enter a number: "))

        if stringChoice == 1:
            string = str(input("Please enter a string: "))
            output = vowels(string)
            print("There are",output,"vowels in the string")

        elif stringChoice == 2:
            string1 = str(input("Please enter a string: "))
            encryption(string1)

        else:
            print("The value you have input is invalid.")
            print("Please try again.")

    else:
        print("The value you have input is invalid.")
        print("Please try again.")
        
main()