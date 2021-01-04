#I pledge my Honor that I have abided by the Stevens Honor System - Joseph Rotundo
#I understand that I may access the course textbook and course lecture notes but I am not to access any other resource.
#I also pledge that I worked alone on this exam.

def main():
    start = input("Enter 1 for Mathematical Functions.\nEnter 2 for String Operations.\n")
    start = int(start)
    if start == 1:
        math = input("\nFor addition, please enter the number 1. \nFor subtraction, please enter the number 2. \nFor multiplication, please enter the number 3. \nFor division, please enter the number 4.\n")
        math = int(math)
        if math == 1:
            a = float(input("\nEnter the first number you wish to add: "))
            b = float(input("\nEnter the second number you wish to add: "))
            sum = a+b
            print("\nThe sum is:", sum)
        elif math == 2:
            c = float(input("\nEnter the first number you wish to subtract \n(The second number will be subtracted from the first number): "))
            d = float(input("\nEnter the second number you wish to subtract: "))
            dif = c-d
            print("\nThe difference is:", dif)
        elif math == 3:
            e = float(input("\nEnter the first number you would like to multiply: "))
            f = float(input("\nEnter the second number you would like to multiply: "))
            product = round(e*f, 4)
            print("\nThe product is:", product)
        elif math == 4:
            g = float(input("\nEnter the first number you would like to divide \n(The first number will be divided by the second number): "))
            h = float(input("\nEnter the second number you would like to divide: "))
            quotient = round(g/h, 4)
            print("\nThe answer is:", quotient)
        else:
            print("\nERROR! Please run program again and enter a number between 1 and 4.")
    elif start == 2:
        stringer = input("\nTo determine the number of vowels in a string, enter the number 1. \nTo encrypt a string, enter the number 2.\n")
        stringer= int(stringer)
        if stringer == 1:
            string = input("\nEnter the string: ")
            vowel1 = string.count("a")
            vowel2 = string.count("e")
            vowel3 = string.count("i")
            vowel4 = string.count("o")
            vowel5 = string.count("u")
            sum2 = vowel1 + vowel2 + vowel3 + vowel4 + vowel5
            print("\nThere are", sum2, "vowels in the string.")
        elif stringer == 2:
            message = input("\nEnter the message you would like to encrypt: ")
            print("\nThe encrypted message is: ")
            for i in message:
                x = ord(i)
                print(" ", x*x+x-2, end = "")
        else:
            print("\nERROR! Please run program again and enter the number 1 or 2.") 
    else:
        print("\nERROR! Please run program again and enter the number 1 or 2.")

main()
    
    
