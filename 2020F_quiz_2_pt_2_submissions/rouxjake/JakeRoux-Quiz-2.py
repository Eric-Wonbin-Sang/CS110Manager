#I pledge my Honor that I have abided by the Stevens Honor System. Jake Roux

def main():
    print("For Mathematical Functions, Please Enter the Number 1")
    print("For String Operations, Please Enter the Number 2")
    choice = input("Enter 1 or 2 Here:")

    if choice == "1":
        print("For Addition, Please Enter the Number 1")
        print("For Subtraction, Please Enter the Number 2")
        print("For Multiplication, Please Enter the Number 3")
        print("For Division, Please Enter the Number 4")

        choice2 = input("Please enter the number of the function:")

        if choice2 == "1":
            print("This function will perform Addition")
            num1 = int(input("Enter the first number to add:"))
            num2 = int(input("Enter the Number to be added to the first number:"))
            ans = num1 + num2
            print("The sum of the two numbers is:", ans)

        elif choice2 == "2":
            print("This function will perform Subtraction")
            num1 = int(input("Enter the first number to subtract:"))
            num2 = int(input("Enter the number to be subtracted from the first number:"))
            ans = num1 - num2
            print("The difference is:", ans)

        elif choice2 == "3":
            print("This function will perform Multiplication")
            num1 = int(input("Enter the first number to multiply:"))
            num2 = int(input("Enter the number to be multiplied to the first number:"))
            ans = num1 * num2
            print("The product is:", ans)

        elif choice2 == "4":
            print("This function will perform Division")
            num1 = int(input("Enter the first number to divide:"))
            num2 = int(input("Enter the number to by divided from the first number:"))
            ans = num1 / num2
            print("The quotient is:", ans)

        else:
            print("Please enter a valid number between 1 and 4")

    elif choice == "2":
        print("To Determine the Number of Vowels in a String; Enter the Number 1")
        print("To Encrypt a String; Enter the Number 2")

        choice2 = input("Please enter the number of the function:")

        if choice2 == "1":
            wrd = input(print("Please enter the word or sentence you would like to count the vowels of:"))
            vowels = ["A","a","E","e","I","i","O","o","U","u"]
            tot = 0
            for letter in wrd:
                if letter in vowels:
                    tot += 1
            print("The number of vowels is:", tot)

        elif choice2 == "2":
            wrd = input(print("Enter the word or sentence you would like to encrypt:"))
            print("Below is your encrypted message:")
            for i in wrd:
                x = ord(i)
                print("", x+5, end= "")

        else:
            print("Please select 1 or 2")
    else:
        print("Please select 1 or 2")

main()

