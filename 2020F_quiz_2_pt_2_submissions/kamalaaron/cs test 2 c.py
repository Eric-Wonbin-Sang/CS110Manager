# Aaron Kamal
# I pledge that I have abided by the stevens honor system
def main():
    ans=True
    print("""
    1. Enter 1 for a mathematical function
    2. Enter 2 for a string operation
    """)
    if ans != "1" or "2":
        print("This is not valid")
    ans = input("What would you like to do?")
    if ans == "1":
        print("Math Function")
        print("""
        1. Enter 1 for addition
        2. Enter 2 for subtraction
        3. Enter 3 for multiplication
        4. Enter 4 for division
        """)
        ans2= input("What would you like to do?")
        if ans2 == "1":
            print("Addition")
            num1=int(input("Enter the first number:"))
            num2=int(input("Enter the second number:"))
            add=num1+num2
            print("The sum of the two numbers is:",add)
            
        elif ans2 == "2":
            print("Subtraction")
            num1=int(input("Enter the first number:"))
            num2=int(input("Enter the second number:"))
            sub=num1-num2
            print("The difference of the two numbers is:",sub)
        
        elif ans2 == "3":
            print("Multiplication")
            num1=int(input("Enter the first number:"))
            num2=int(input("Enter the second number:"))
            mul=num1*num2
            print("The product of the two numbers is:",mul)
        
        elif ans2 == "4":
            print("Division")
            num1=int(input("Enter the first number:"))
            num2=int(input("Enter the second number:"))
            div=num1/num2
            print("The quotient of the two numbers is:",div)
        
        else:
            print("Not a valid option")
    elif ans == "2":
        print("String operation")
        print("""
        1. Enter 1 to determine the number of vowels in a string
        2. Enter 2 to encrypt a string
        """)
        ans3= input("What would you like to do?")
        if ans3 == "1":
            print("Vowels in a string")
            inputstr = str(input("Please type a sentence to have the vowels counted:"))
            vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
            count= 0
            for letter in inputstr:
                if letter in vowel:
                    count+=1
            print(count)
                
        elif ans3 == "2":
            print("Encrypt a string")
            def main():
                message= input("Enter a message to encode:")
                for i in message:
                    print(ord(i), end=" ")
                print()
            main()
        else:
            print("This is not a valid option")
            
            
    else:
        print("Not a valid option")
main()





