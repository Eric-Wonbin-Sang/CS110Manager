#I pledge my honor that I have abided by the Stevens Honor System
#I understand that I may access the course textbook and course lecture notes but I am not to access any other resource. I also pledge that I worked alone on this exam.
#Dmitriy Stepanyan

def arithmetic(arithmetic_choice):
        if arithmetic_choice == 1:
            numbers = input("\nEnter two numbers you would like to add"
                            "\nseparated by a space:")
            list = numbers.split()
            newlist = [int(i) for i in list]

            sum = newlist[0]+newlist[1]

            print("\n The sum:", sum)

        elif arithmetic_choice == 2:
            numbers = input("\nEnter two numbers you would like to subtract"
                            "\nseparated by a space:")
            list = numbers.split()
            newlist = [int(i) for i in list]
            diff = newlist[0] - newlist[1]

            print("\n The difference:", diff)

        elif arithmetic_choice == 3:
            numbers = input("\nEnter two numbers you would like to multiply"
                            "\nseparated by a space:")
            list = numbers.split()
            newlist = [int(i) for i in list]

            product = newlist[0]*newlist[1]

            print("\n The product:", product)

        elif arithmetic_choice == 4:
            numbers = input("\nEnter two numbers you would like to divide"
                            "\nseparated by a space:")
            list = numbers.split()
            newlist = [int(i) for i in list]
            quotient = newlist[0]/newlist[1]
            print("\n The quotient:", quotient)

        else:
            print("\nError! The value entered is not a viable choice!")

def manipulation(string_choice):
    if string_choice == 1:
        text = input("\nInput a string:")
        text = text.lower()

        string = ""

        for i in text:
            if i == "a" or i == "e" or i == "u" or i == "o" or i == "i":
                string = string + i
            else:
                string = string

        print("\nThe number of vowels:", len(string))

    elif string_choice == 2:
        text = input("\nInput a string:")

        string = ""

        for n,i in enumerate(text):
            if i == " ":
                x = 32
                string = string + chr(x)

            #BELOW: Removing the word 'and' and replacing
            #it with a single character

            #This is done to make code-breaking harder
            #as the easiest code-breaking techniques target
            #the most common short words that can be identified
            #such as 'I', 'and', 'am', etc.

            elif text[n - 1] == " " and i == "a" and text[n + 1] == "n" and text[n + 2] == "d" and text[n + 3] == " ":
                x = 100
                string = string + chr(x)
            elif text[n - 2] == " " and text[n - 1] == "a" and i == "n" and text[n + 1] == "d" and text[n + 2] == " ":
                string = string
            elif text[n - 3] == " " and text[n - 2] == "a" and text[n - 1] == "n" and i == "d" and text[n + 1] == " ":
                string = string
            ##################

            #Replacing the word 'I' with a fixed character
            #'I' will be replaced in any position (first, middle,last)

            elif n != 0 and len(text) - n != 1 and text[n - 1] == " " and i =="I" and text[n + 1] == " " \
                    or text[0] == "I" and n == 0 and text[n + 1] == " " \
                    or text[n - 1] == " " and i == "I" and len(text) - n == 1:
                x = 99
                string = string + chr(x)

            #Replacing the word 'am' with a single character (in middle of text)

            elif n != 0 and len(text) - n != 1 and text[n - 1] == " " and i == "a" and text[n + 1] == "m" and text[n + 2] == " ":
                x = 98
                string = string + chr(x)
            elif text[n - 2] == " " and text[n - 1] == "a" and i == "m" and text[n + 1] == " ":
                string == string
            #################

            #Replacing the article 'a' with a fixed character

            elif n != 0 and len(text) - n != 1 and text[n - 1] == " " and i == "a" and text[n + 1] == " " \
                    or text[0] == "A" and n == 0 and text[n + 1] == " ":
                x = 101
                string = string + chr(x)


            else:
                x = (ord(i)*5+22)
                string = string + chr(x)

        print(string)

    else:
        print("\nError! The value entered is not a viable choice!")


def main():
    mathorstring = int(input("For Mathematical Functions: Enter the Number 1 "
                         "\nFor String Operations: Enter the Number 2:"))

    if mathorstring == 1:
        arithmetic_choice = int(input("\nFor Addition: Enter the Number 1 "
              "\nFor Subtraction: Enter the Number 2 "
              "\nFor Multiplication: Enter the Number 3 "
              "\nFor Division: Enter the Number 4:"))
        arithmetic(arithmetic_choice)

    elif mathorstring == 2:
        string_choice = int(input("\nTo Determine the Number of Vowels in a String: Enter the Number 1 "
              "\nTo Encrypt a String: Enter the Number 2:"))
        manipulation(string_choice)

    else:
        print("\nError! The value entered is not a viable choice!")

main()