#I pledge my Honor that I have abided by hte Stevens Honor System Phu-Quy Ho
print("For Mathematical Functions, Please Enter the Number 1")
print("For String Operations, Please Enter the Number 2")
x = int(input(""))
if x == 1:
    print("For Addition, Please Enter the Number 1")
    print("For Subtraction, Please Enter the Number 2")
    print("For Multiplication, Please Enter the Number 3")
    print("For Division, Please Enter the Number 4")
    y = eval(input(""))
    if y == 1:
        number1 = int(input("What is your first number?"))
        number2 = int(input("What is your second number?"))
        result = number1 + number2
    elif y == 2:
        number1 = int(input("What is your first number?"))
        number2 = int(input("What is your second number?"))
        result = number1 - number2
    elif y == 3:
        number1 = int(input("What is your first number?"))
        number2 = int(input("What is your second number?"))
        result = number1 * number2
    elif y == 4:
        number1 = int(input("What is your first number?"))
        number2 = int(input("What is your second number?"))
        result = number1/number2
    else:
        print("Error")
    print(result)
elif x == 2:
    print("To Determine the Number of Vowels in a String; Enter the Number 1")
    print("To Encrypt a String; Enter the Number 2")
    y = eval(input(""))
    if y == 1:
        string = input("Enter your string")
        lowercase = string.lower()
        vowel_counts = {}
        for vowel in "aeiou":
            count = lowercase.count(vowel)
            vowel_counts[vowel] = count
        print("There are " + vowel_counts + "vowels in your string")
    elif y == 2:
        string = input("Enter your string")
        res = (string*3)[len(string)+4:2*len(string)+4]
        print(res)

    else:
        print("Error")
else:
    print("Error")
