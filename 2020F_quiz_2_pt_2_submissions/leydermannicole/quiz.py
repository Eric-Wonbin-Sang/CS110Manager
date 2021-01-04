#I pledge my Honor that I have abided by the Stevens honor system
def main():
    menu()
def menu():
    print("For Mathematical Functions, Please Enter the Number 1")
    print("For String Operations, Please Enter the Number 2")
    choice = input("\nPlease enter your choice: ")

    if choice == "1":
        print("For Addition, Please Enter the Number 1\nFor Subtraction, Please Enter the Number 2")
        print("For Multiplication, Please Enter the Number 3\nFor Division, Please Enter the Number 4")
        choice1 = input("\nPlease enter your choice: ")

        if choice1 == "1":
            def main():
                def sum1(x,y):
                    sum = x + y
                    return sum
                print("Enter two numbers separated by a comma:")
                num1, num2 = input().split(",")
                add = sum1(float(num1), float(num2))
                print("The sum is",(add))
            main()

        elif choice1 == "2":
            def main():
                def diff1(x,y):
                    diff= x - y
                    return diff
                print("Enter two numbers separated by a comma:")
                num1, num2 = input().split(",")
                subtract =diff1(float(num1), float(num2))
                print("The difference is", (subtract))
            main()

        elif choice1 == "3":
            def main():
                def mult1(x,y):
                    mult= x * y
                    return mult
                print("Enter two numbers separated by a comma:")
                num1, num2 = input().split(",")
                multiply =mult1(float(num1), float(num2))
                print("The product is", (multiply))
            main()

        elif choice1 == "4":
            def main():
                def div1(x, y):
                    div = x / y
                    return div
                print("Enter two numbers separated by a comma:")
                num1, num2 = input().split(",")
                divide = div1(float(num1), float(num2))
                print("The quotient is", (divide))
            main()

        else:
            print("You must only select either 1 or 2, Please try again")

    elif choice == "2":
        print ("To Determine the Number of Vowels in a String, Enter the Number 1")
        print("To Encrypt a String; Enter the Number 2")
        choice2 = input("\nPlease enter your choice: ")
        string=input("Enter a string: ")

        if choice2 == "1":
            string.lower()
            vowels = 0
            for i in string:
                if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
                    vowels = vowels + 1
            print("Number of vowels are:",vowels)

        elif choice2 == "2":
            print("\nHere is the encrypted string:")
            for i in string:
                x = ord(i)
                print("",x + 5,end="")

        else:
            print("You must only select either 1 or 2, Please try again")

    else:
        print("You must only select either 1 or 2")
        print("Please try again")
        menu()

main()