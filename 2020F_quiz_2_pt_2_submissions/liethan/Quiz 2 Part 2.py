def main():
    start = input("Please enter 1 for mathematical functions, or enter 2 for string operations: ")
    if start == "1":
        math = input("Please enter 1 for addition, 2 for subtraction, 3 for multiplication, or 4 for division: ")
        if math == "1":
            input1 = float(input("Please enter the first number: "))
            input12 = float(input("Please enter the number you would like to add to the first number: "))
            add = input1 + input12
            print(add, "is the sum of the two numbers entered")
        elif math == "2":
            input2 = float(input("Please enter the first number: "))
            input22 = float(input("Please enter the number you would like to subtract from the first number: "))
            sub = input2 - input22
            print(sub, "is the difference of the two numbers entered")
        elif math == "3":
            input3 = float(input("Please enter the first number: "))
            input32 = float(input("Please enter the number you would like to multiply with the first number: "))
            mul = input3 * input32
            print(mul, "is the product of the two numbers entered")
        elif math == "4":
            input4 = float(input("Please enter the first number: "))
            input42 = float(input("Please enter the number you would like to add to the first number: "))
            div = input4 / input42
            print(div, "is the quotient of the two numbers entered")
        else:
            print("That is not a valid input")
    elif start == "2":
        inputs = input(
            "Please enter 1 if you would like to determine the number of vowels in a string, or enter 2 if you would like to encrypt a string: ")
        if inputs == "1":
            message = input("Please enter the string you would like to determine the number of vowels in: ")
            lowermessage = message.lower()
            count = 0
            a = lowermessage.count("a")
            count = count + a
            e = lowermessage.count("e")
            count = count + e
            i = lowermessage.count("i")
            count = count + i
            o = lowermessage.count("o")
            count = count + o
            u = lowermessage.count("u")
            count = count + u
            print("There are", count, "vowels in your string")
        elif inputs == "2":
            message = input("Please enter the string you would like to encrypt: ")
            print("This is the encrypted message")
            for i in message:
                x = ord(i)
                print("", 2 * x + 3, end="")
            print()
        else:
            print("That is not a valid input")
    else:
        print("That is not a valid input")

main()