#Quiz Two Part Two
#I pledge my honor that I have abided by the Stevens honor system -Maya O

def main():
    print("Hello!")
    print("Please enter 1 if you would like to access the mathematical funtions")
    print("Please enter 2 if you would like to access the string operations")
    m = int(input("Choice: "))

    def error():
        print()
        print("Error: You entered a number that was not one of the menu options")
        print("Please trying running the code from the beginning")
    def thanks():
        print()
        print("Thanks for using this program!")

    if m == 1:
        print()
        print("Great! Now, ")
        print("For addition, please enter 1")
        print("For subtraction, please enter 2")
        print("For multiplication, please enter 3")
        print("For division, please enter 4")
        math = int(input("Choice: "))
        if math ==1:
            print()
            print("Please enter 2 numbers")
            num1 = int(input("Number 1: "))
            num2 = int(input("Number 2: "))
            addition = num1 + num2
            print("The sum of these two numbers is" , addition)
            thanks()
        elif math==2:
            print()
            print("Please enter 2 numbers")
            num1 = int(input("Number 1: "))
            num2 = int(input("Number 2: "))
            subtraction = num1 - num2
            print("The difference between these two numbers is" , subtraction)
            thanks()
        elif math==3:
            print()
            print("Please enter 2 numbers")
            num1 = int(input("Number 1: "))
            num2 = int(input("Number 2: "))
            multiplication = num1 * num2
            print("The product of these two numbers is" , multiplication)
            thanks()
        elif math==4:
            print()
            print("Please enter 2 numbers")
            num1 = int(input("Number 1: "))
            num2 = int(input("Number 2: "))
            division = round(num1 / num2, 3)
            print("The quotient of these two numbers is" , division)
            thanks()
        elif math>4 or math<1:
            error()

    elif m == 2:
        print()
        print("Great! Now,")
        print("To determine the number of vowels in a string, please enter 1")
        print("To encrypt a string, please enter 2")
        stringop= int(input("Choice: "))
        if stringop==1:
            print()
            string = str(input("Please enter a string: "))
            count = 0
            vowel = set("aeiouAEIOU")
            for letters in string:
                if letters in vowel:
                    count = count + 1
            if count == 1:
                print("There is" , count , "vowel in the given string")
            else:
                print("There are" , count , "vowels in the given string")
            thanks()

        elif stringop==2:
            print()
            string = input("Please enter a string: ")
            print("Here is the encrypted message:")
            for i in string:
                x=ord(i)
                print("",2*x+3,end="")
            thanks()

        elif stringop>2 or stringop<1:
            error()

    elif m>2 or m<1:
        error()

main()
