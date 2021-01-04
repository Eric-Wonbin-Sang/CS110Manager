Mathematical_Functions = "For Mathematical Functions, Please Enter the Number 1"
String_Operations = "For String Operations, Please Enter the Number 2"
Instruction1="Enter 1 or 2:"
Math_Chosen = "You have selected the Mathematical Functions Menu"
String_Chosen = "You have selected the String Operations Menu"
Addition_Operation = "For Addition, Please Enter the Number 1"
Subtraction_Operation = "For Subtraction, Please Enter the Number 2"
Multiplication_Operation = "For Multiplication, Please Enter the Number 3"
Division_Operation = "For Division, Please Enter the Number 4"
Determine_Number_of_Vowels_Operation = "To Determine the Number of Vowels in a String; Enter the Number 1"
Encrypt_a_String_Operation = "To Encrypt a String of Characters; Enter the Number 2"
Switch_to_Math = "To switch to the Mathematical Functions, Please Enter the Number 5"
Switch_to_String = "To switch to the String Functions, Please Enter the Number 5"
Math_Function_Disclaimer = "You will be asked to enter two numbers. An error message will appear after BOTH numbers are entered, if you have not put in a valid number."

def String_Function():
    print(String_Chosen)
    print("")
    String_Instructions()
    print("")
    string_choice = input("Please enter 1, 2, or 5:")
    print("")
    if string_choice == "1":
        Count_Vowels_Function()
        Menu_Selection()
    elif string_choice == "2":
        Encryption_Function()
        Menu_Selection()
    elif string_choice == "5":
        Math_Function()
    else:
        print("Error Message. Try again.")
        String_Function()

def Math_Function():
    print(Math_Chosen)
    print("")
    Math_Instructions()
    print("")
    math_choice = input("Please enter 1, 2, 3, 4, or 5:")
    print("")
    if math_choice == "1":
        Addition_Function()
        Menu_Selection()
    elif math_choice == "2":
        Subtraction_Function()
        Menu_Selection()
    elif math_choice == "3":
        Multiplication_Function()
        Menu_Selection()
    elif math_choice == "4":
        Division_Function()
        Menu_Selection()
    elif math_choice == "5":
        String_Function()
    else:
        print("Error Message. Try again.")
        Math_Function()

def Menu_Instructions():
    print(Mathematical_Functions)
    print(String_Operations)

def Math_Instructions():
    print(Addition_Operation)
    print(Subtraction_Operation)
    print(Multiplication_Operation)
    print(Division_Operation)
    print(Switch_to_String)

def Addition_Function():
    X = str(input("Please enter a number being added:"))
    if X.isdecimal():
        X = X
    else:
        print("Error Message. Try again.")
        Addition_Function()
    Y = str(input("Please enter a number being added:"))
    if Y.isdecimal():
        Y = Y
    else:
        print("Error Message. Try again.")
        Addition_Function()
    if X.isdecimal() and Y.isdecimal():
        print("The sum is:", int(X) + int(Y))
        print("")
        Menu_Selection()
    else:
        print("Error Message. Try again.")
        Addition_Function()

def Subtraction_Function():
    X = str(input("Please enter a number being subtracted from:"))
    if X.isdecimal():
        X = X
    else:
        print("Error Message. Try again.")
        Subtraction_Function()
    Y = str(input("Please enter a number being subtracted by:"))
    if Y.isdecimal():
        Y = Y
    else:
        print("Error Message. Try again.")
        Subtraction_Function()
    if X.isdecimal() and Y.isdecimal():
        print("The difference is:", int(X) - int(Y))
        print("")
        Menu_Selection()
    else:
        print("Error Message. Try again.")
        Subtraction_Function()

def Multiplication_Function():
    X = str(input("Please enter a number being multiplied:"))
    if X.isdecimal():
        X = X
    else:
        print("Error Message. Try again.")
        Multiplication_Function()
    Y = str(input("Please enter a number being multiplied by:"))
    if Y.isdecimal():
        Y = Y
    else:
        print("Error Message. Try again.")
        Multiplication_Function()
    if X.isdecimal() and Y.isdecimal():
        print("The product is:", int(X) * int(Y))
        print("")
        Menu_Selection()
    else:
        print("Error Message. Try again.")
        Multiplication_Function()

def Division_Function():
    X = str(input("Please enter a number being divided:"))
    if X.isdecimal():
        X = X
    else:
        print("Error Message. Try again.")
        Division_Function()
    Y = str(input("Please enter a number being divided by:"))
    if Y.isdecimal():
        Y = Y
    else:
        print("Error Message. Try again.")
        Division_Function()
    if X.isdecimal() and Y.isdecimal():
        print("The quotient is:", int(X) / int(Y))
        print("")
        Menu_Selection()
    else:
        print("Error Message. Try again.")
        Division_Function()

def String_Instructions():
    print(Determine_Number_of_Vowels_Operation)
    print(Encrypt_a_String_Operation)
    print(Switch_to_Math)

def Count_Vowels_Function():
    print("This function will count the amount of vowels in a string.")
    String1 = input("Please enter a sentence, phrase, word, or other expression:")
    Vowels = 0
    for v in String1:
        if (v == "A" or v == "a" or v == "E" or v == "e" or v == "I" or v == "i"
                or v == "O" or v == "o" or v == "U" or v == "u"):
            Vowels = Vowels + 1
    print("Vowel Count:", Vowels)
    print("")

def Encryption_Function():
    print("This function will encrypt a string.")
    Message = input("Please enter a sentence, phrase, word, or other expression:")
    for v in Message:
        x = ord(v)
        print((x+70)*2, end = str((x+15)*3))
        if (v == "a"):
            print(end = str(x*3-10))
    print("")
    print("")



def Menu_Selection():
    Menu_Instructions()
    print("")
    choice = input(Instruction1)
    print("")
    if choice =="1":
        Math_Function()
    elif choice =="2":
        String_Function()
    else:
        print("Error Message. Try again.")
        Menu_Selection()

Menu_Selection()
