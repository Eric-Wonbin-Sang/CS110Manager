#MatthewMascoloQuiz2
#I pledge my honor that I have abided
#by the Stevens Honor System. Matthew Mascolo
#
#Coding segment to Quiz #2

def addition(num1, num2):
    ans = int(num1) + int(num2)
    return ans

def subtraction(num1, num2):
    ans = int(num1) - int(num2)
    return ans

def multiplication(num1, num2):
    ans = int(num1) * int(num2)
    return ans

def division(num1, num2):
    ans = int(num1) / int(num2)
    return ans

def vowelCount(sentence):
    vowel = 0

    for char in sentence:
        if char in "AEIOUaeiou":
            vowel = vowel+1
    return vowel

def encrypt(string): #Encrpyts a string using the encryption code we learned in class
    newString = ""
    for i in string:
        x = ord(i)
        newString = newString + str(x+5) + " "
    return newString

def main():

    answer = input("For Mathematical Functions Please Enter the Number 1\nFor String Operations Please Enter the Number 2\n")

    if answer == "1":
        answerMath = input("For Addition, Please Enter the Number 1\nFor Subtraction, Please Enter the Number 2\nFor Multiplication, Please Enter the Number 3\nFor Division, Please Enter the Number 4\n")

        if answerMath.isdigit() == False:
            raise Exception("Please enter a numerical digit.")
        else:
            if int(answerMath) == 1 or int(answerMath) == 2 or int(answerMath) == 3 or int(answerMath) == 4:
                if int(answerMath) == 1: #Addition Section of Mathimatical Functions
                    number1 = input("Enter first number:")
                    if number1.isdigit() == False:
                        raise Exception("Please enter a numerical digit.") #Exception is thrown when number 1 is not a number.
                    
                    number2 = input("Enter second number:")
                    if number2.isdigit() == False:
                        raise Exception("Please enter a numerical digit.") #Exception is thrown when number 2 is not a number.
                    
                    ans = addition(number1, number2)
                    print("The sum of", number1, "and", number2, "is:", ans)
                else:
                    if int(answerMath) == 2: #Subtraction Section of Mathimatical Functions
                        subnum1 = input("Enter first number:")
                        if subnum1.isdigit() == False:
                            raise Exception("Please enter a numerical digit.") #Exception is thrown when number 1 is not a number.

                        subnum2 = input("Enter second number:")
                        if subnum2.isdigit() == False:
                            raise Exception("Please enter a numerical digit.") #Exception is thrown when number 2 is not a number.

                        subAns = subtraction(subnum1, subnum2)
                        print("The difference between", subnum1, "and", subnum2, "is:", subAns)
                    else:
                        if int(answerMath) == 3: #Multiplication Section of Mathematical Functions
                            num1 = input("Enter first number:")
                            if num1.isdigit() == False:
                                raise Exception("Please enter a numerical digit.") #Exception is thrown when number 1 is not a number.
                            num2 = input("Enter second number:")
                            if num2.isdigit() == False:
                                raise Exception("Please enter a numerical digit.") #Exception is thrown when number 2 is not a number.

                            product = multiplication(num1, num2)
                            print("The product of", num1, "and", num2, "is:", product)
                        else:
                            if int(answerMath) == 4:#Division Section of Mathematical Functions
                                divnum1 = input("Enter first number:")
                                if divnum1.isdigit() == False:
                                    raise Exception("Please enter a numerical digit.") #Exception is thrown when number 1 is not a number.

                                divnum2 = input("Enter second number:")
                                if divnum2.isdigit() == False:
                                    raise Exception("Please enter a numerical digit.") #Exception is thrown when number 2 is not a number.

                                divAns = division(divnum1, divnum2)
                                print("The qoutient of", divnum1, "and", divnum2, "is:", divAns)
            else:
                raise Exception("Out of range error. Please enter numbers 1, 2, 3, or 4.")
    else:
        if answer == "2":
            answerString = input("To Determine How Many Vowels Are In A String, Enter 1.\nTo Encrypt A String, Enter 2.\n")

            if answerString.isdigit() == False:
                raise Exception("Please enter a numerical digit.")
            else:
                if int(answerString) == 1 or int(answerString) == 2:
                    if int(answerString) == 1: #Vowel Counting Section of String Functions
                        enteredString = input("Enter a string:")
                        vowelCounted = vowelCount(enteredString)
                        print("There amount of vowels in the string you entered is:", vowelCounted)
                    else:
                        if int(answerString) == 2: #Encrypting String Section
                            encryptString = input("Enter a string:")
                            encryptedString = encrypt(encryptString)
                            print("The Encrypted String is:", encryptedString)
                            
                else:
                    raise Exception("Out of range error. Please enter numbers 1, or 2.")
                    

        else:
            if answer.isdigit():
                raise Exception("Out of range error. Please enter number 1 or 2.")
            else:
                if isinstance(answer, str):
                    raise Exception("Please enter a numerical digit.")
               
main()
