#"I pledge my honor that I've abided by the stevens honor system" -Nicholas DiGiacomo
def add(a,b):
    c= a + b 
    return c
def sub(a,b):
    c = a - b
    return c
def multi(a,b):
    c = a*b
    return c
def div(a,b):
    c=a/b
    return c
def vowels(string):
    count = 0
    for i in range(len(string)):
        a = string[i]
        if a == "a" or a == "e" or a == "i" or a== "o" or a == "u":
            count = count + 1
        elif a == "A" or a == "E" or a == "I" or a == "O" or a== "U":
            count = count + 1
    return count
def encrypt(string_two):
    for i in string_two:
        x = ord(i)
        print("", x + 10,end="")
    
            
def main():

    try:
    
        print("Enter 1 for mathematical operations")
        print("Enter 2 for string operations:")
        numberinput1 = int(input("Enter a number from 1 to 2:")) 
        if numberinput1 == 1:
            print("Please enter 1 for addition:")
            print("Please enter 2 for subtraction:")
            print("Please enter 3 for multiplication:")
            print("Please enter 4 for divison:")
            numberinput2 = int(input("Enter your number:"))
            num1 = int(input("Enter the first number:"))
            num2 = int(input("Enter the second number:"))

            if numberinput2 == 1:
                result1 = add(num1, num2)
                print("Here's the result:",result1)
            elif numberinput2 == 2:
                result2 = sub(num1, num2)
                print("Here's the result:",result2)
            elif numberinput2 == 3:
                result3 = multi(num1, num2)
                print("Here's the result:",result3)
            elif numberinput2 == 4:
                result4 = div(num1, num2)
                print("Here's the result:",result4)
            else:
                print("Something went wrong, please try again")
        

        elif numberinput1 == 2:
            print("Enter number 1 for vowel count")
            print("Enter number 2 for encryption")
            numberinput3 = int(input("Enter the number:"))
            string = str(input("Enter the string:"))

            if numberinput3 == 1:
                result5 = vowels(string)
                print("Here's the number of vowels:",result5)
            elif numberinput3 == 2:
                print("Here's your encrypted message:")
                encrypt(string)
            
            else:
                print("Something went wrong, please try again")

    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("Something went wrong, please try again")
        else:
            print("Something went wrong, please try again")
        
main()
        
            
        
            
        
    
