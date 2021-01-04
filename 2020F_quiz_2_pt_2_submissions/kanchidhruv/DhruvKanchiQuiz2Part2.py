# I pledge my Honor that I have abided by the Stevens Honor System.

def main():
    programSelection = int(input(" Please enter 1 for Mathematical Functions and 2 for String Operations."))
    if programSelection == 1:
        mathSelection = int(input("For addition, please enter the number 1, for subtraction, please enter the number 2, For multiplication, please enter the number 3, and for division, please enter the number 4."))
        if mathSelection == 1:
            print("You have selected addition.")
            x = int(input("Enter the first addend."))
            y = int(input("Enter the second addend."))
            sum1 = x + y
            print("The sum is", sum1)

        if mathSelection == 2:
            print("You have selected subtraction.")
            x = int(input("Enter the first number."))
            y = int(input("Enter the second number."))
            difference = x - y
            print("The difference is", difference)
            
        if mathSelection == 3:
            print("You have selected multiplication.")
            x = int(input("Enter the first number."))
            y = int(input("Enter the second number."))
            product = x * y
            print("The product is", product)
            
        if mathSelection == 4:
            print("You have selected division.")
            x = int(input("Enter the dividend."))
            y = int(input("Enter the divisor."))
            quotient = x / y
            print("The quotient is", quotient)
            
        if mathSelection < 1 or mathSelection > 4:
            print("This is an invalid input.")
            
    if programSelection == 2:
        stringSelection = int(input("To determine the number of vowels in the string, please enter the number 1, to encrypt a string, please enter the number 2."))

        if stringSelection == 1:
            string1 = str(input("Please enter a string."))
            a = string1.count("a")
            e = string1.count("e")
            i = string1.count("i")
            o = string1.count("o")
            u = string1.count("u")
            y = string1.count("y")
            a1 = string1.count("A")
            e1 = string1.count("E")
            i1 = string1.count("I")
            o1 = string1.count("O")
            u1 = string1.count("U")
            y1 = string1.count("Y")
            vowelCount = a + e + i + o + u + y + a1 + e1 + i1 + o1 + u1 + y1
            print("The number of vowels in this string is", vowelCount)

        if stringSelection == 2:
            string1 = str(input("Please enter the string you want to encrypt."))
            for i in string1:
                encryptedString = ord(i)
                print(" ", encryptedString + 11, end = "")
            print()
    if programSelection != 1 and programSelection != 2:
        print("This is an invalid input.")


main()
                
        
