# Catherine Maloney - CS 110 Quiz 2 Part 2
# I pledge my honor that I have abided by the Stevens honor system.
# I understand that I may access the course textbook and course lecture notes
# but I am not to access any other resource. I also pledge that I worked alone
# on this exam.

# This program performs Python operations based on the selections the user inputs.

def main():

    menu = int(input("For Mathematical Functions, Please Enter the Number 1;"
                     "\nFor String Operations, Please Enter the Number 2: "))
    if menu != 1 or 2:
        print("Your menu entry is invalid.")
        
    if menu == 1:
        math = int(input("For Addition, Please Enter the Number 1;"
                         "\nFor Subtraction, Please Enter the Number 2;"
                         "\nFor Multiplication, Please Enter the Number 3;"
                         "\nFor Division, Please Enter the Number 4: "))

        if math == 1:
            x = int(input("Enter integer 1 to be added: "))
            y = int(input("Enter integer 2 to be added: "))
            add = x + y
            print("The sum of the integers you entered is: ",add)
        elif math == 2:
            x = int(input("Enter integer 1 to be subtracted: "))
            y = int(input("Enter integer 2 to be subtracted: "))
            sub = x - y
            print("The difference of the integers you entered is: ",sub)
        elif math == 3:
            x = int(input("Enter integer 1 to be multiplied: "))
            y = int(input("Enter integer 2 to be multiplied: "))
            mult = x*y
            print("The product of the integers you entered is: ",mult)
        elif math == 4:
            x = int(input("Enter integer 1 to be divided: "))
            y = int(input("Enter integer 2 to be divided: "))
            divide = x/y
            print("The quotient of the integers you entered is: ",divide)
        else:
            print("Your menu entry is invalid.")
       
    if menu == 2:
        string = int(input("To Determine the Number of Vowels in a String; Enter the Number 1;"
                           "\nTo Encrypt a String; Enter the Number 2: "))
        
        if string == 1:
            str_input = str(input("Enter a string that will have its vowels counted: "))
            count = 0
            vowels = ["A","a","E","e","I","i","O","o","U","u"]
            for letter in str_input:
                if letter in vowels:
                    count += 1
            print("The number of vowels in your string is: ",count)

        elif string == 2:
            str_input = str(input("Enter a string to be encyrpted: "))
            print("Your encrypted string is: ")
            for i in str_input:
                print(ord(i), end = "")
                
        else:
            print("Your menu entry is invalid.")

main()
