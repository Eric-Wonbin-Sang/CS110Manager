#Saumit Madireddy

#I pledge my Honor that I have abided by the Stevens Honor System
#I understand that I may access the course textbook and course lecture notes but
#I am not to access any other resource. I also pledge that I worked alone on this exam.

def main():
    menu()

def menu():
    choice = input("""
    For Mathematical Functions, Please Enter the Number 1
    For String Operations, Please Enter the Number 2
    """)

    if choice == "1":
        math()
    elif choice == "2":
        english()
    else:
        print("You must only select either 1 or 2")
        print("Please try again")
        menu()

def math():
    choice = input("""
    For Addition, Please Enter the Number 1 
    For Subtraction, Please Enter the Number 2
    For Multiplication, Please Enter the Number 3
    For Division, Please Enter the Number 4
    """)

    if choice == "1":
        x = eval(input("Enter Number 1: "))
        y = eval(input("Enter Number 2: "))
        theSum = x + y
        print(theSum)
    elif choice == "2":
        x = eval(input("Enter Number 1: "))
        y = eval(input("Enter Number 2: "))
        sub = x - y
        print(sub)
    elif choice == "3":
        x = eval(input("Enter Number 1: "))
        y = eval(input("Enter Number 2: "))
        mult = x * y
        print(mult)
    elif choice == "4":
        x = eval(input("Enter Number 1: "))
        y = eval(input("Enter Number 2: "))
        div = x / y
        print(div)
    else:
        print("You must only select either 1,2,3, or 4")
        print("Please try again")
        math()

def english():
    choice = input("""
    To Determine the Number of Vowels in a String; Enter the Number 1
    To Encrypt a String; Enter the Number 2
    """)

    if choice == "1":
        string1 = input("Enter a Word: ")
        count = 0
        vowel = set("aeiouAEIOU")
        for alphabet in string1:
            if alphabet in vowel:
                count = count + 1
        print("No. of vowels :", count)
    elif choice == "2":
        string1 = input("Enter a Word: ")
        print("\nHere is the encrypted Word:")
        for i in string1:
            x = ord(i)
            print(" ", x + 5, end = "")
    else:
        print("You must only select either 1 or 2")
        print("Please try again")
        english()
    
main()
