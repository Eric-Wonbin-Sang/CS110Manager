#I pledge my Honor that I have abided by the Stevens Honor System.

#I understand that I may access the course textbook and course lecture notes but I am not to access any other resource.
#I also pledge that I worked alone on this exam.

#Melissa Atmaca

def addition(x, y):
    sum = x + y
    return sum

def subtraction(x, y):
    diff = x - y
    return diff

def multiplication(x, y):
    prod = x * y
    return prod

def division(x, y):
    div = x / y
    return div

def vow(string):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    count = 0
    for vowel in vowels:
        if vowel in string:
            count += 1
    print("The vowel count in the string is", count)

def encrypt(string):
    for i in string:
        print(ord(i), end=" ")
    return



def main():

    select = int(input("For Mathematical Functions, Please Enter the Number 1.\nFor String Operations, Please Enter the Number 2:\n"))

    if select == 1:
        matop = int(input("For Addition, Please Enter the Number 1\nFor Subtraction, Please Enter the Number 2\nFor Multiplication, Please Enter the Number 3\nFor Division, Please Enter the Number 4: \n"))
        if matop == 1:
            num1, num2 = input("Please enter two numbers separated by a comma: ").split(",")
            a = addition(float(num1), float(num2))
            print(a)
        elif matop == 2:
            num1, num2 = input("Please enter two numbers separated by a comma: ").split(",")
            a = subtraction(float(num1), float(num2))
            print(a)
        elif matop == 3:
            num1, num2 = input("Please enter two numbers separated by a comma: ").split(",")
            a = multiplication(float(num1), float(num2))
            print(a)
        elif matop == 4:
            num1, num2 = input("Please enter two numbers separated by a comma: ").split(",")
            division(float(num1), float(num2))
            print(a)
        else:
            print("Your entry is invalid. Please input a numerical character that is within the numerical range.")
    elif select == 2:
        stringop = int(input("To Determine the Number of Vowels in a String; Enter the Number 1\nTo Encrypt a String; Enter the Number 2:\n"))
        if stringop == 1:
            str = input("Please input a string: ")
            vow(str)
        elif stringop == 2:
            str = input("Please input a string: ")
            encrypt(str)
        else:
            print("Your entry is invalid. Please input a numerical character that is within the numerical range.")

    else:
        print("Your entry is invalid. Please input a numerical character that is within the numerical range.")


main()




