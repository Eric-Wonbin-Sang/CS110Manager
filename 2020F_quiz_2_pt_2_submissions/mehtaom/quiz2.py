def add():
    x = int(input("Enter your first number."))
    y = int(input("Enter your second number."))
    z = x + y
    print("The sum of these numbers is", z)



def subtract():
    x = int(input("Enter your first number."))
    y = int(input("Enter your second number."))
    z = x - y
    print("The difference of these numbers is", z)



def multiply():
    x = int(input("Enter your first number."))
    y = int(input("Enter your second number."))
    z = x * y
    print("The product of these numbers is", z)



def divide():
    x = int(input("Enter your first number."))
    y = int(input("Enter your second number."))
    z = x / y
    print("The quotient of these numbers is", z)



def string1():
    string = str(input("Enter a string."))
    vowels = 'aeiou'
    count = 0
    for s in string:
        if s in vowels: count = count + 1
    print("There are", count, "vowels in this string.")

def string2():
    message = input("Enter a message to encode.")
    print("\n Here is the encrypted message.")
    for i in message:
        x = ord(i)
        print(" ", x + 5, end="")
    print()

def main():
    global message
    choice = int(input("For mathematical functions, please enter the number 1.\nFor String Operations, please enter the number 2."))
    if choice == 1:
        operation = int(input("For Addition, Please Enter the Number 1. \nFor Subtraction, Please Enter The Number 2. \nFor Multiplication, Please Enter the Number 3. \nFor Division, Please Enter the Number 4."))
        if operation == 1:
            add()
        elif operation == 2:
            subtract()
        elif operation == 3:
            multiply()
        elif operation == 4:
            divide()
        else: print("Please only enter a number ranging 1-4.")
    if choice == 2:
        x = int(input("To Determine the Number of Vowels in a String; Enter the Number 1 \nTo Encrypt a String; Enter the Number 2"))
        if x == 1:
            string1()
        elif x == 2:
            string2()
    else: print("Please only enter a number ranging 1-2.")
    if choice != 1 and choice != 2:
        print("Please only enter a number ranging 1-2.")
main()


