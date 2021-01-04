# I pledge my honor that I have abided by the Stevens Honor System
# Gabrielle Armetta

# a Python program which will present the user with a menu of items to select
# the user will select a menu item and the program will perform the operation

def main():
    print("For Mathematical Functions, Please Enter the Number 1")
    print("For String Operations, Please Enter the Number 2")
    choice1 = input("Enter the integer:")
    if choice1 == "1":
        print("For Addition, Please Enter the Number 1")
        print("For Subtraction, Please Enter the Number 2")
        print("For Multiplication, Please Enter the Number 3")
        print("For Division, Please Enter the Number 4")
        choice2 = input("Enter the integer:")
        print("Please Enter 2 Integers")
        x = input("Enter the first integer:")
        y = input("Enter the second integer:")

        if choice2 == "1":
            print(int(x) + int(y))
        elif choice2 == "2":
            print(int(x) - int(y))
        elif choice2 == "3":
            print(int(x) * int(y))
        elif choice2 == "4":
            print(int(x) / int(y))
        else:
            print("The Input is Invalid")
    elif choice1 == "2":
        print("To Determine the Number of Vowels in a String; Enter the Number 1")
        print("To Encrypt a String; Enter the Number 2")
        choice3 = input("Enter the integer:")
        a_string = input("Enter a string:")
        if choice3 == "1":
            vowels = 0
            for i in a_string:
                if(i == 'A' or i == 'a' or i == 'E' or i == 'e' or i == 'I' or i == 'i' or i == 'O' or i == 'o' or i == 'U'or i == 'u'):
                    vowels = vowels+1
            print("Number of vowels is:")
            print(vowels)
        elif choice3 == "2":
            for i in a_string:
                x = ord(i)
                print("", x + 2, end = "")
        else:
            print("The Input is Invalid")
    else:
        print("The Input is Invalid")


if __name__ == "__main__":
    main()