#I pledge my Honor that I have abided by the Stevens Honor System.
#I understand that I may access the course textbook and course lecture notes but I am not to access any other resource.
#I also pledge that I worked alone on this exam.
#Meher Kohlli
def Mathematicalfunction():
    print("\nMATHEMATICAL FUNCTIONS")
    print("For addition, please enter 1")
    print("For subtraction, please enter 2")
    print("For multiplication, please enter 3")
    print("For division, please enter 4")
        
    entry = float(input("Enter a number: "))
    
    num1 = float(input("\nEnter your first number: "))
    num2 = float(input("\nEnter your second number: "))

    if entry == 1:
        print(num1 + num2)
    elif entry == 2:
        print (num1 - num2)
    elif entry == 3:
        print(num1 * num2)
    elif entry == 4:
        print(num1 / num2)

    else:
        print("Invalid selection")

def Stringfunctions():
    print("\nSTRING FUNCTIONS")
    print("To determine the number of vowels in a string, please enter 1")
    print("To encrypt a string, please enter 2")

    selection = float(input("Enter a number: "))
    if selection < 1 or selection > 2:
        print("Invalid selection")
    else:
        string = input("Enter a string of words: ")

        if selection == 1:
            vowels = 0
            for i in string:
                if (i == 'a' or i == 'e' or i == 'o' or i == 'u' or i == 'y' or i == 'i' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or i == 'Y'):
                    vowels = vowels + 1
            print("The number of vowels in", string, "are: ", vowels)

        elif selection == 2:
            for i in string:
                x = ord(i)
                new = (x + 10) * 3
            print("the encrypted message is: ", new)

        else:
            print("Invalid selection")
def main():
    def mainmenu():
        print("\nMAIN MENU")
        print("For mathematical functions, please enter 1")
        print("For string functions, please enter 2")

    mainmenu()
    choice = float(input("Enter a choice: "))

    if choice == 1:
        Mathematicalfunction()
    elif choice == 2:
        Stringfunctions()
    else:
        print("Invalid selection")


    
main()

