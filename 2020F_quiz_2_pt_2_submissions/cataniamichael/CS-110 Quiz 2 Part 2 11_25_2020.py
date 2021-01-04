# I pledge my Honor that I have abided by the Stevens Honor System
# I understand that I may access the course textbook and course lecture notes
# but I am not to access any other resources.
# I also pledge that I worked alone on this exam
def math():
    print("Enter 1 for Addition.")
    print("Enter 2 for Subtraction.")
    print("Enter 3 for Multiplication.")
    print("Enter 4 for Dividion.")
    mch = int(input("Enter the number that corresponds to your choice:"))
    if mch == 1:
        x = float(input("Enter the first number:"))
        y = float(input("Enter the second number:"))
        print(x + y)
    elif mch == 2:
        x = float(input("Enter the first number:"))
        y = float(input("Enter the second number:"))
        print(x - y)
    elif mch == 3:
        x = float(input("Enter the first number:"))
        y = float(input("Enter the second number:"))
        print (x * y)
    elif mch == 4:
        x = float(input("Enter the first number:"))
        y = float(input("Enter the second number:"))
        print(x / y)
    else:
        print("This entry is invalid")
def string():
    print("Enter 1 to find the number of vowels in your string.")
    print("Enter 2 to encrypt your string.")
    sch = int(input("Enter 1 for Vowels or 2 for Encryption:"))
    if sch == 1:
        v = input("Enter a string:")
        count = 0
        vow = set("aeiouAEIOU")
        for i in v:
            if i in vow:
                count = count + 1
        print("There are", count, "vowels in your string")
    elif sch == 2:
        mes = input("Enter a string:")
        print("\nYour encrypted message is:")
        for i in mes:
            x = ord(i)
            print(" ",x+21, end="")
    else:
        print("This entry is invalid")
def main():
    print("To access Mathimatical Functions, enter 1.")
    print("To access String Operations, enter 2.")
    ch = int(input("Enter 1 for Math or 2 for Strings:"))
    if ch == 1:
        return math()
    elif ch == 2:
        return string()
    else:
        print("This entry is invalid")
main()

        
            
    

    

