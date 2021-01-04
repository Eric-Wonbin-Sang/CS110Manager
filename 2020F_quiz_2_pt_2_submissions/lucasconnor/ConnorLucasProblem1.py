#Pledge: I pledge my Honor that I have abided by the Stevens Honor System

#I understand that I may access the course textbook and course lecture notes but I am not to access any other resource.
# #I also pledge that I worked alone on this exam.

#Number 1

def main():
    ans =True
    print("Enter 1 for mathmatical function or 2 for a string operation")
    ans = input("Which one do you prefer?")
    if ans != "1" or "2":
        print("This is not a valid statement")
    if ans == "1":
        print("Math Function")
        print("""
        1. 1 is addition
        2. 2 is subtraction
        3. 3 is multiplication
        4. 4 is division
        """)
        ans2 = input("What would you like to do?")
        if ans2 == "1":
            print ("Addition")
            firstnum = int(input("Enter a number to be added"))
            secondnum = int(input("Enter a number to be added to firstnum"))
            add = firstnum + secondnum
            print("The sum of the equation is:", add)
        elif ans2 == "3":
            print("multiplication")
            firstnum = int(input("Enter number 1"))
            secondnum = int(input("Enter a number to be multiplied by number 1"))
            product = firstnum * secondnum
            print("The product is", product)
        elif ans2 == "2":
            print("subtraction")
            firstnum = int(input("Enter the first number"))
            secondnum = int(input("Enter  a number to be subtracted from the 1st number"))
            difference = firstnum - secondnum
            print("Your answer is", difference)
        elif ans2 == "4":
            print("division")
            firstnum = int(input("Type the numerator"))
            secondnum = int(input("Type in the denominator"))
            quotient = firstnum / secondnum
            print("The solution is", quotient)
        else:
            print("This is not a valid option")
    elif ans == "2" :
        print("This is a string operation")
        print("1 counts vowels and 2 encrypts a string")
        ans3 = input(print("What would you like to do?"))
        if ans3 == "1":
            input(print("Vowel Counter"))
            inputstr = str(input("Type a sentence"))
            vowel = ['a', 'e', i, 'o', 'u', 'A', 'E', 'I', 'O', 'U']
            count = 0
            for letter in inputstr:
                if letter in vowel:
                    count += 1
            print(count)
        elif ans3 == "2":
            print("String Encryption")
            def main():
                encryption = input(print("Enter something to be encrypted"))
                for i in encryption:
                    print(ord(i), end = " ")
            main()
main()





