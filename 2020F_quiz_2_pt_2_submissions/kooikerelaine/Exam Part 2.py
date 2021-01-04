#I pledge my Honor that I have abided by the Stevens Honor System. 
#I understand that I may access the course textbook and course lecture notes but I am not to access any other resource.
#I also pledge that I worked alone on this exam. Elaine Kooiker


def add(x,y):
    result=x+y
    return result
def subtract(x,y):
     result=x-y
     return result
def multiply(x,y):
     result=x*y
     return result
def divide(x,y):
     result=float(x/y)
     return result
    
def vowels(word):
    count=0
    for i in word:
        if (i == "a"):
            count+=1
        elif (i == "e"):
            count+=1
        elif (i ==  "i"):
            count+=1
        elif (i == "o"):
            count+=1
        elif (i == "u"):
            count+=1
        elif(i=="y"):
            count+=1
    return count
def encrypt(word):
    newword=[]
    for i in word:
        x=(ord(i))
        x=(((((x*8)+6)*2)+8)/2)
        newword.append(x)
    return newword


def main():
#Prompt user to enter 1 for mathematical fnctions or 2 for string operations
    firstInput=input("Enter 1 for mathematical functions or 2 for string operations: ")

    if firstInput=="1":
        print("For Addition, Please Enter the Number 1")
        print("For Subtraction, Please Enter the Number 2")
        print("For Multiplication, Please Enter the Number 3")
        print("For Division, Please Enter the Number 4")
        secondInput=input("Enter a number 1, 2, 3, or 4: ")
        if secondInput ==("1"):
                x=int(input("Enter a first number to add: "))
                y=int(input("Enter the second number: "))
                add(x,y)
                print (x,"+", y, "=", add(x,y))
        if secondInput ==("2"):
                x=int(input("Enter a first number: "))
                y=int(input("Enter the number to subtract: "))
                subtract(x,y)
                print (x,"-", y, "=",subtract(x,y))
        if secondInput ==("3"):
                x=int(input("Enter a first number: "))
                y=int(input("Enter the second number: "))
                multiply(x,y)
                print (x,"*", y, "=",multiply(x,y))
        if secondInput ==("4"):
                x=int(input("Enter the first number: "))
                y=int(input("Enter the divisor: "))
                divide(x,y)
                print (x,"/", y, "=",divide(x,y))
        else:
                print("Errror: You did not enter a number 1 through 4")
    elif firstInput=="2":
        print("To Determine the Number of Vowels in a String; Enter the Number 1")
        print("To Encrypt a String; Enter the Number 2")
        secondInput=input("Enter a number 1 or 2: ")
        #After the user enters the menu number, prompt them to enter a string and then perform the selected string operation
        #and return the result.
        if secondInput=="1":
                word=str(input("Enter a string: "))
                print(vowels(word))
        if secondInput=="2":
                word=str(input("Enter a string: "))
                print(encrypt(word))
        else:
            print("Error: you did not enter 1 or 2.")
    else:
        print("Error: You did not enter a number 1 or 2")
#Please Note; if the user enters an invalid entry for any menu item, you should return an error message. (Examples of invalid entries for the menu item would include a number which is out-of-range or a non-numerical character).

main()
