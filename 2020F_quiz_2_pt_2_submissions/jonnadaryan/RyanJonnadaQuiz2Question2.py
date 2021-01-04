#Ryan Jonnada
#I pledge my honor that I have abided by the Stevens Honor System

def main():
    print("For Mathematical Functions, Please Enter the Number 1")
    print("For String Operations, Please Enter the Number 2")
    ans = input()
    if ans == "1":
        print("For Addition, Please Enter the Number 1")
        print("For Subtraction, Please Enter the Number 2")
        print("For Multiplication, Please Enter the Number 3")
        print("For Division, Please Enter the Number 4")

        ans2 = input("Which Mathematical Function would you like to perform?")
        if ans2 == "1":
            print ("You have selected Addition")
            num1 = int(input("Enter a number for addition"))
            num2 = int(input("Enter a number to be added to the first number"))
            add = num1 + num2
            print("The result of this addition problem is:", add)
        elif ans2 == "2":
            print ("You have selected Subtraction")
            num1 = int(input("Enter a number for subtraction"))
            num2 = int(input("Enter a number to be subtracted from the first number"))
            sub = num1 - num2
            print("The result of this subtraction problem is", sub)
        elif ans2 == "3":
            print("You have selected Multiplication")
            num1 = int(input("Enter a number for multiplication"))
            num2 = int(input("Enter a number to be multiplied by the first number"))
            mult = num1 * num2
            print("The result of this multiplication problem is", mult)
        elif ans2 == "4":
            print("You have selected Division")
            num1 = int(input("Enter a number for division"))
            num2 = int(input("Enter a number to be divided by the first problem"))
            div = num1 / num2
            print("The result of this division problem is", div)
        else:
            print("This is not a valid selection, please select a number between 1 and 4")
    elif ans =="2":
        print("To Determine the Number of Vowels in a String; Enter the Number 1")
        print("To Encrypt a String; Enter the number 2")
        ans3 = input("Would you like to determine the number of vowels in a string or encrypt a string")
        if ans3 == "1":
            input(print("You have decided to count the number of vowels in a string, please enter a sentence"))
            vowel = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
            count = 0
            for letter in inputstr:
                if letter in vowel:
                    count += 1
            print(count)
        elif ans3 == "2":
            print("You have decided to encrypt a string")
            def main():
                message = input("Enter message to encode:")
                print("\nHere is the encrypted message:")
                for i in message:
                    x = ord(i)
                    print("", x+5, end = "")
                print()
            main()
        else:
            print("This is not a valid selction, please select either 1 or 2")
main()
    
