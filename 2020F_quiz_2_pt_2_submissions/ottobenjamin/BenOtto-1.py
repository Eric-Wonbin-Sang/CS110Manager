#Pledge: I pledge my Honor that I have abided by the Stevens Honor System
#Ben Otto

#I understand that I may access the course textbook and course lecture notes but
#I am not to access any other resource. I also pledge that I worked alone on this exam.


#Math Operations

def addition(x,y):
    return (x+y)

def subtraction(x,y):
    return(x-y)

def multiplication(x,y):
    return(x*y)

def division(x,y):
    if (y==0):
        return("Divide by Zero Error")
    else:
        return (x/y)

#String Operations

def count_vowels (word):
    word=word.lower()
    count=word.count("a")+word.count("e")+word.count("i")+word.count("o")+word.count("u")
    return count

def encrypt (word):
    word2=""
    for i in range(len(word)):
        word2+=str(chr(ord(word[i])+i))
    return word2

def main():
        num1=int(input("Enter 1 for mathematical operation, 2 for string operation"))
        if (num1==1):
            num2=int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division"))
            nums=input("Enter the two numbers you wish to perform the operation on separated by a comma").split(",")
            x=int(nums[0])
            y=int(nums[1])
            if num2==1:
                print(addition(x,y))
            elif num2==2:
                print(subtraction(x,y))
            elif num2==3:
                print(multiplication(x,y))
            elif num2==4:
                print(division(x,y))
            else:
                print("You entered an invalid operation")
                main()
        elif (num1==2):
            num2=int(input("Enter 1 for counting vowels, enter 2 for encryption"))
            word=input("Enter the string to perform the operation on")
            if (num2==1):
                print(count_vowels(word))
            elif(num2==2):
                print(encrypt(word))
            else:
                print("You entered an invalid operation")
                main()
        else:
            print("You entered an invalid operation")
            main()
main()