#I pledge my honor that I have abided by the Stevens Honor System
#I understand that I may access the course textbook and course lecture notes but I am not to
#access any other resource. I also pledge that I worked alone on this exam.



#PLEASE NOTE THAT I DID NOT CONSIDER "Y" A VOWEL. THE CHOICE TO LEAVE IT OUT WAS INTENTIONAL ***



def main():
    first = int(input("For mathematical functions, Please Enter the number 1\nFor String Operations, Please Enter the Number 2\n"))

    if first == 1:
        mathops(first)
    if first == 2:
        stringops(first)
    else:
        print("Error: you have entered an invalid command\n")
        exit()

def mathops(first):
    num1 = int(input("For Addition, Please Enter the Number 1\nFor Subtraction, Please Enter the Number 2\nFor Multiplication, Please Enter the Number 3\nFor Division, Please Enter the Number 4\n"))
    if num1 ==1:
        a = int(input("Enter a number\n"))
        b = int(input("Enter a number\n"))
        ans = a + b
        print("Your result is", ans)
        exit()

    if num1 ==2:
        c = int(input("Enter a number\n"))
        d = int(input("Enter a number\n"))
        ans2 = c - d
        print("Your result is", ans2)
        exit()

    if num1 ==3:
        e = int(input("Enter a number\n"))
        f = int(input("Enter a number\n"))
        ans3 = e * f
        print("Your result is", ans3)
        exit()

    if num1 ==4:
        g = int(input("Enter a number\n"))
        h = int(input("Enter a number\n"))
        ans4 = g / h
        print("Your result is", ans4)
        exit()

    else:
        print("Error: you have entered an invalid command\n")
        exit()

def stringops(first):
    num1 = int(input("To Determine the Number of Vowels in a String; Enter the Number 1\nTo Encrypt a String; Enter the Number 2\n"))

    if num1 ==1:
        str1 = str(input("Enter your string: \n"))
        vowels = 0
        for i in str1:
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
                vowels = vowels + 1
        print("There are ",vowels, "vowels in your string.")
        exit()

    if num1 ==2:
        str1 = str(input("Enter your string: \n"))
        print("Your encrypted message in digits is:")
        for i in str1:
             print(ord(i) + 3)
        exit()

    else:
        print("Error: you have entered an invalid command\n")
        exit()

main()