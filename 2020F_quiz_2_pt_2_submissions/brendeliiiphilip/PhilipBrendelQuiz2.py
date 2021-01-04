##Philip Brendel
##I pledge my Honor that I have abided by the Stevens Honor System
##I understand that I may access the course textbook and course lecture notes but I am not to access any other resource. I also pledge that I worked alone on this exam.

def encrypt(message):
    code = []
    encrypt_string = []
    for i in message:
        x = ord(i)
        code.append(x + 3)
   # print(code)
    for i in code:
        codeNum = int(i)
        encrypt_string.append(chr(codeNum))
        encrypt_string_out ="".join(encrypt_string)
    
    return encrypt_string_out
    #print(encrypt_string_out)

def vowels(string):
    count = 0
    for i in string:
        if i in 'aeiouy':
            count += 1

    return count


    
def add(x,y):
    
    ans = x + y
    return ans

def sub(x,y):
    ans = x - y
    return ans

def div(x,y):
    ans = x/y
    return ans

def mult(x,y):
    ans = x * y
    return ans

def main():
    print("For Mathematical Functions, Please Enter the Number 1")
    ask = int(input("For String Operations, Please Enter the Number 2 "))
    if ask == 1:
        print("For Addition, Please Enter the Number 1")
        print("For Subtraction, Please Enter the Number 2")
        print("For Multiplication, Please Enter the Number 3")
        ask3 = int(input("For Division, Please Enter the Number 4 "))
        if ask3 != 1 and ask3 != 2 and ask3 != 3 and ask3 != 4:
            print("Error, invalid input entered.")
        else:
            x = int(input("Enter your first number: "))
            y = int(input("Enter your second number: "))
            if ask3 == 1:
                print("Your sum is: ", add(x,y))
            if ask3 == 2:
                print("Your difference is: ", sub(x,y))
            if ask3 == 3:
                print("Your answer is: ", mult(x,y))
            if ask3 == 4:
                print("Your answer is: ", div(x,y))
    
    elif ask == 2:
        print("To Determine the Number of Vowels in a String; Enter the Number 1")
        ask2 = int(input("To Encrypt a String; Enter the Number 2 "))
        if ask2 == 1:
            string = input("Please enter the string you would like to use: ")
            print("There are",vowels(string), "vowels in", string)
        elif ask2 == 2:
            message = input("Please enter the string you want encrypted: ")
            print("Your encrypted string is: ", encrypt(message))
        else:
             print("Error, invalid input entered.")

    else:
        print("Error, invalid input entered.")



main()
