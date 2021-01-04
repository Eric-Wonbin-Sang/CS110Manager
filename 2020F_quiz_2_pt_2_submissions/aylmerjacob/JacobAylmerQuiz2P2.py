# I pledge my honor I have abided by the Stevens Honor System
# I understand that I may access the course textbook and course lecture notes
# but I am not to access any other resource.
# I also pledge that I worked alone on this exam.
# Jacob Aylmer
# Quiz 2 Part 2

def main():

    math_or_string = float(input("Enter 1 for mathematical function or 2 for string functions: "))
    if math_or_string == 1:
        print("These are the math functions")
        math_operations = float(input("Enter 1 for for addition, 2 for subtraction, 3 for multiplication or 4 for division: "))
        if math_operations == 1:
            print("Add two numbers")
            add1 = float(input("Enter first number to add: "))
            add2 = float(input("Enter second number to add: "))
            sum1 = add1 + add2
            print(sum1)
        elif math_operations == 2:
            print("Subtract two numbers")
            sub1 = float(input("Enter first number to subtract: "))
            sub2 = float(input("Enter second number to subtract: "))
            difference1 = sub1 - sub2
            print(difference1)
        elif math_operations == 3:
            print("Multiply two numbers")
            mult1 = float(input("Enter first number to multiply: "))
            mult2 = float(input("Enter second number to multiply: "))
            product1 = mult1 * mult2
            print(product1)
        elif math_operations == 4:
            print("Divide two numbers")
            div1 = float(input("Enter first number to divide: "))
            div2 = float(input("Enter second number to divide: "))
            quotient1 = div1 / div2
            print(quotient1)
        else:
            print("Invalid input")
    elif math_or_string == 2:
        print("These are the string functions")
        string_operations = float(input("Enter 1 to count the number of vowels in a string or enter 2 to encrypt a string: "))
        if string_operations == 1:
            print("This will count the number of vowels in a string")
            str1 = input("Enter a string: ")
            a1 = str1.count("a") + str1.count("A")
            e1 = str1.count("e") + str1.count("E")
            i1 = str1.count("i") + str1.count("I")
            o1 = str1.count("o") + str1.count("O")
            u1 = str1.count("u") + str1.count("U")
            y1 = str1.count("y") + str1.count("Y")
            vowels1 = a1 + e1 + i1 + o1 + u1 + y1
            print(vowels1)
        elif string_operations == 2:
            print("This will encrypt a string")
            str2 = input("Enter a string: ")
            for i in str2:
                x = ord(i)
                print("", x + 5, end = "")
            print()
        else:
            print("Invalid input")
    else:
        print("Invalid input")





main()
