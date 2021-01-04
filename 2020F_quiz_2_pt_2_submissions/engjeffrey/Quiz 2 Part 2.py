# I pledge my honor that I have abided by the Stevens Honor System.
# I understand that I may access the course textbook and course lecture notes but I am not to access any other resource.
# I also pledged that I worked alone on this exam.
# Jeffrey Eng

def add(a,b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    result = a / b
    return result

def vowels(string):
    count = 0
    for i in string.lower():
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            count = count + 1
        else:
            count = count
    return count

def encrypt(string):
    encrypted_message = ""
    for i in string:
        x = int(ord(i) * 1000 / 234 + 15)
        encrypted_message = encrypted_message + str(x) + " "
    return encrypted_message

def main():
    try:
        print("Main Menu Items:")
        print("For Mathematical Functions, Please Enter The Number 1")
        print("For String Operations, Please Enter The Number 2")
        main_menu = int(input("\nEnter The Appropriate Main Menu Item Number: "))
        if main_menu == 1:
            print("\nMathematical Functions:")
            print("For Addition, Please Enter The Number 1")
            print("For Subtraction, Please Enter The Number 2")
            print("For Multiplication, Please Enter The Number 3")
            print("For Division, Please Enter The Number 4")
            math_function = int(input("\nEnter The Appropriate Mathematical Function Number: "))
            if math_function == 1:
                a = float(input("\nEnter The First Number To Be Used In The Calculation: "))
                b = float(input("Enter The Second Number to Be Used In The Calculation: "))
                print("\nThe Sum Is", add(a,b))
            elif math_function == 2:
                a = float(input("\nEnter The First Number To Be Used In The Calculation: "))
                b = float(input("Enter The Second Number To Be Used In The Calculation: "))
                print("\nThe Difference Is", subtract(a,b))
            elif math_function == 3:
                a = float(input("\nEnter The First Number To Be Used In The Calculation: "))
                b = float(input("Enter The Second Number To Be Used In The Calculation: "))
                print("\nThe Product Is", multiply(a,b))
            elif math_function == 4:
                a = float(input("\nEnter The First Number To Be Used In The Calculation: "))
                b = float(input("Enter The Second Number To Be Used In The Calculation: "))
                print("\nThe Quotient Is", divide(a,b))
            else:
                print("\nError: You Did Not Enter A Valid Mathematical Function Item Number")
        elif main_menu == 2:
            print("\nString Operations:")
            print("To Determine The Number Of Vowels In A String; Enter The Number 1")
            print("To Encrypt A String; Enter the Number 2")
            string_op = int(input("\nEnter The Appropriate String Operation Number: "))
            if string_op == 1:
                input_string = str(input("\nEnter A String To Determine The Number Of Vowels: "))
                print("There Are", vowels(input_string), "Vowel(s) In Your String")
            elif string_op == 2:
                input_string = str(input("\nEnter A String To Encrypt: "))
                print("Your Encrypted Message Is: ", encrypt(input_string))
            else:
                print("Error: You Did Not Enter A Valid String Operation Item Number")
        else:
            print("\nError: You Did Not Enter A Valid Main Menu Item Number")
    except ValueError as excObj:
        if "invalid literal for int()" in str(excObj):
            print("\nError: You Entered A Non-Numerical Character")
        elif "could not convert string to float" in str(excObj):
            print("\nError: You Entered A Non-Numerical Character")
        else:
            print("\nError: Other ValueError")
    except ZeroDivisionError as excObj:
        if "float division by zero" in str(excObj):
            print("\nError: You Cannot Divide By Zero")
        else:
            print("\nError: Other ZeroDivisionError")
main()
