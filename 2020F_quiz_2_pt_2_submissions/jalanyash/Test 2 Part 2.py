#I pledge my Honor that I have abided by the Stevens Honor System
#I understand that I may access the course textbook and course lecture notes but I am not to access any other resource.
# I also pledge that I worked alone on this exam.

def main():
    numorstring = int(input("For Mathematical Functions, Please Enter the Number 1.\nFor String Operations, Please Enter the Number 2.\nWhich option would you lke to select?"))
    if numorstring ==1 :
        mathoption = int(input("For Addition, Please Enter the Number 1. \nFor Subtraction, Please Enter the Number 2. \nFor Multiplication, Please Enter the Number 3. \nFor Division, Please Enter the Number 4.\nWhich option would you lke to select?"))
        if mathoption == 1:
            num = float(input("Enter your first number: "))
            num1 = float(input("Enter your second number: "))
            addition = num+num1
            print(addition)
        elif mathoption == 2:
            num2 = float(input("Enter your first number: "))
            num3 = float(input("Enter your second number: "))
            subtraction = num2 - num3
            print(subtraction)
        elif mathoption == 3:
            num4 = float(input("Enter your first number: "))
            num5 = float(input("Enter your second number: "))
            multiplication = num4 * num5
            print(multiplication)
        elif mathoption == 4:
            num6 = float(input("Enter your first number: "))
            num7 = float(input("Enter your second number: "))
            division = num6 / num7
            print(division)
        else:
            print("Error:Your entry is invalid")

    if numorstring == 2:
        stringoption = int(input("To Determine the Number of Vowels in a String; Enter the Number 1.\nTo Encrypt a String; Enter the Number 2.\nWhich option would you lke to select?"))
        if stringoption == 1:
            string =input("Enter a string: ")
            a = string.count("a") + string.count("A")
            e = string.count("e") + string.count("E")
            i = string.count("i") + string.count("I")
            o = string.count("o") + string.count("O")
            u = string.count("u") + string.count("U")
            y = string.count("y") + string.count("Y")
            vowels = a+e+i+o+u+y
            print(vowels)
        elif stringoption == 2:
            string1 =input("Enter a string: ")
            for i in string1:
                x = ord(i)
                print(" ",x + 5,end ="")
            print()
        else:
            print("Error:Your entry is invalid")
main()