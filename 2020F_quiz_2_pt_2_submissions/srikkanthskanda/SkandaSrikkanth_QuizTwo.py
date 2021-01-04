# I pledge my honor that I have abided by the Stevens Honor System

# I understand that I may access the course textbook and course lecture notes but I am not to access any other resource.
# I also pledge that I worked alone on this exam.

def python_operations():
    i = int(input("Please enter '1' for mathematical functions and '2' for string operations: "))
    if i != 1 and i != 2:
        raise ValueError(f"Invalid code {i}. Must be 1 or 2")
        
    if i == 1:
        print("Mathematical Operations")
        j = int(input("Enter '1' for Addition, '2' for Subtraction, '3' for Multiplication, and '4' for Division: "))
        if j != 1 and j != 2 and j != 3 and j != 4:
            raise ValueError(f"Invalid code {j}. Must be a number from 1 to 4")

        if j == 1:
            k = int(input("You will now enter two numbers. Enter the first: "))
            l = int(input("Enter the second. This will be added to the first: "))
            total = k + l
            print("The sum is " + str(total))
        if j == 2:
            k = int(input("You will now enter two numbers. Enter the first: "))
            l = int(input("Enter the second. This number will be subtracted from the first: "))
            result = k - l
            print("The result is " + str(result))
        if j == 3:
            k = int(input("You will now enter two numbers. Enter the first: "))
            l = int(input("Enter the second. This will be multiplied by the first: "))
            product = k * l
            print("The product is " + str(product))
        if j == 4:
            k = int(input("You will now enter two numbers. Enter the first: "))
            l = int(input("Enter the second. The first will be divided by this number: "))
            quotient = k / l
            print("The quotient is " + str(quotient))


    if i == 2:
        print("String Operations")
        m = int(input("Enter '1' to determine the number of vowels and '2' to encrypt a string: "))
        if m != 1 and m != 2:
            raise ValueError(f"Invalid code {m}. Must be 1 or 2")

        if m == 1:
            vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
            number = 0
            n = input("Enter a string of letters, and it will return the number of vowels: ")
            for o in range(len(n)):
                if n[o] in vowels:
                    number = number + 1
            print("The number of vowels in this string is " + str(number))
        if m == 2:
            code = []
            group_one = ['a', 'b', 'c', 'd', 'e', 'f']
            group_two = ['g', 'h', 'i', 'j', 'k', 'l']
            group_three = ['m', 'n', 'o', 'p', 'q', 'r', 's']
            group_four = ['t', 'u', 'v', 'w', 'x', 'y', 'z']
            p = input("Enter a string of lowercase letters, and it will encrypt it for you: ")
            for x in range(len(p)):
                if p[x] in group_one:
                    code.append(1)
                elif p[x] in group_two:
                    code.append(2)
                elif p[x] in group_three:
                    code.append(3)
                elif p[x] in group_four:
                    code.append(4)
            print()
            print("The encrypted code, in a list, is: ")
            print(code)


python_operations()