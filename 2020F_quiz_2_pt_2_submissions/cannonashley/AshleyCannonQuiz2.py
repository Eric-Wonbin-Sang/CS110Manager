# I pledge my honor that I have abided by the Stevens Honor System
# Ashley Cannon

def addition():
    num1 = input("Enter a number:" )
    num2 = input("Enter the seccond number:")
    sum = num1 + num2
    print(sum)
def subtraction():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    ans = num1 - num2
    print(ans)
def multiplication():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    product = num1 * num2
    print(product)
def division():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    quotient = num1 / num2
    print(quotient)
def vowels():
    string = input("Enter a string in all lowercase: ")
    vowels = 0
    for i in string:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            vowels = vowels+1
    print(vowels)
def encrypt():
    string = input("Enter a string: ")
    for i in string.split:
        print(ord(i) + 4)
def main():
    option1 = input("For Mathematical functions, Please Enter the number 1:" /n "For String Operations, Please Enter the number 2: ")
    if option1 == 1:
        x = input("For addition, Please Enter the Number 1:" /n "For Subtraction, Please Enter the number 2:" /n "For Multiplication, Please Enter the Number 3:" /n "For division, Please Enter the Number 4:")
    if option1 == 2:
        y = input("To Determine the number of Vowels in a string; Enter the Number 1" /n "To Encrypt a string; Enter the Number 2")
    else:
        print("Invalid Option")

    if x == 1:
        addition()
    if x == 2:
        subtraction()
    if x == 3:
        multiplication()
    if x == 4:
        division()
    else:
        print("Invalid Option")

    if y == 1:
        vowels()
    if y == 2:
        encrypt()
    else:
        print("Invalid Option")

main()

        
        
