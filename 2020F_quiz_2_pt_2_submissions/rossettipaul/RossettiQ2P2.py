#I pledge my Honor that I have abided by the Stevens Honor System
#I understand that I may access the course textbook and course lecture notes but I am not to access any other resource. I also pledge that I worked alone on this exam.
#PJ Rossetti

def main():
    print("For mathematical operations, please enter '1'.")
    print("For string operations, please enter '2'.")
    choice = int(input(""))
    if(choice == 1):
        result = 0
        print("For addition, please enter '1'.")
        print("For subtraction, please enter '2'.")
        print("For multiplication, please enter '3'.")
        print("For division, please enter '4'.")
        op = int(input(""))
        num1 = float(input("Enter the first number."))
        num2 = float(input("Enter the second number."))
        if(op == 1):
            result = num1 +num2
        elif(op == 2):
            result = num1 - num2
        elif(op == 3):
            result = num1 * num2
        elif(op == 4):
            result = num1 / num2
            round(result, 2)
        else:
            print("You have entered an invalid number")
        print("The result is :", result)
    elif(choice == 2):
        resultnum = 0
        resultstr = ""
        print("To determine the number of vowels in a string, enter '1'.")
        print("to encrypt a string, enter '2'.")
        op = int(input(""))
        x = input("Enter a string:")
        if(op == 1):
            resultnum = vowel(x)
            print("The result is: ", resultnum)
        elif(op == 2):
            print("The encrypted string is:")
            encrypt(x)
        else:
            print("You have entered an invalid number")
    else:
        print("You have entered an invalid number")


def vowel(i):
    i.lower()
    total = 0
    total += i.count("a")
    total += i.count("e")
    total += i.count("i")
    total += i.count("o")
    total += i.count("u")
    return total
def encrypt(str):
    for i in str:
        x = ord(i)
        print(" ", x+7, end = "")

main()




