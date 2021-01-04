#Sidharth Peri
#11/21/20
#Quiz 2 Part 2

'''Honor Code: I pledge my Honor that I have abided by the Stevens Honor System
I understand that I may access the course textbook and course lecture notes
but I am not to access any other resource. I also pledge that I worked alone on this exam.
Sidharth Peri'''

#A program which presents a user with a menu of items to select and performs operations based on the specific option chosen

def addition_operation(x, y): #function to add 2 numbers
    add_inputs = x + y
    return add_inputs

def subtraction_operation(x, y): #function to subtract 2 numbers
    subtract_inputs = x - y
    return subtract_inputs

def multiplication_operation(x, y): #function to multiply 2 numbers
    multiply_inputs = x*y
    return multiply_inputs

def division_operation(x, y): #function to divide 2 numbers
    divide_inputs = x/y
    return divide_inputs

def count_vowels(string): #function to count the number of vowels in a string
    string = string.lower()
    num_a = string.count('a')
    num_e = string.count('e')
    num_i = string.count('i')
    num_o = string.count('o')
    num_u = string.count('u')

    num_vowels = num_a + num_e + num_i + num_o + num_u 
    return num_vowels

def encrypt_string(string): #function to encrypt a string
    message = []
    for i in string:
        unicodeNum = ((ord(i) * 2) - 10) #algorithm that multiplies the unicode number for each character by 2 and subtracts 10
        unicodeNum = str(unicodeNum)
        message.append(unicodeNum)
    message_output = " ".join(message) #joins list of unicode character strings into one string
    return message_output

def main():
    print("You will need to enter a number to select an option")
    print("For mathematical operations, enter the number 1 and for string operations enter the number 2")

    try: #try except to check for each option (1, 2) and output error message if a non-numerical character is entered
        user_option = int(input("\nPlease enter your option: "))
    
        if(user_option == 1):
            print("You have entered 1 for a mathematical operation")
            print("\nFor Addition, Please Enter the Number 1")
            print("For Subtraction, Please Enter the Number 2")
            print("For Multiplication, Please Enter the Number 3")
            print("For Division, Please Enter the Number 4")
            mathematical_option = int(input("\nPlease enter your option: "))

            try: #try except to check for each option (1-4) and output error message if a non-numerical character is entered
                if(mathematical_option == 1):
                    num1, num2 = input("\nPlease enter two numbers separated by a comma: ").split(",")
                    added_nums = addition_operation(float(num1), float(num2))
                    print(num1, "plus", num2, "is", added_nums)

                elif(mathematical_option == 2):
                    num1, num2 = input("\nPlease enter two numbers separated by a comma: ").split(",")
                    subtracted_nums = subtraction_operation(float(num1), float(num2))
                    print(num1, "minus", num2, "is", subtracted_nums)

                elif(mathematical_option == 3):
                    num1, num2 = input("\nPlease enter two numbers separated by a comma: ").split(",")
                    multiplied_nums = multiplication_operation(float(num1), float(num2))
                    print(num1, "times", num2, "is", multiplied_nums)

                elif(mathematical_option == 4):
                   num1, num2 = input("\nPlease enter two numbers separated by a comma: ").split(",")
                   divided_nums = division_operation(float(num1), float(num2))
                   print(num1, "divided by", num2, "is", divided_nums)

                else: #checks for number out of the range of 1-4 for mathematical operation
                    print("You entered a number out of range. Please enter a number between 1 and 4")

            except ValueError:
                print("Non-numerical character entered. Please enter a number between 1 and 4")
                             
        elif(user_option == 2):
            print("You have entered 2 for a string operation")
            print("\nTo Determine the Number of Vowels in a String; Enter the Number 1")
            print("To Encrypt a String; Enter the Number 2")
            string_option = int(input("\nPlease enter your option: "))

            try: #try except to check for each option (1-2) and output error message if a non-numerical character is entered
                if(string_option == 1):
                    str1 = input("\nPlease enter a string: ")
                    vowels = count_vowels(str1)
                    print("\nThere are", vowels, "vowels in the string: " + str1)

                elif(string_option == 2):
                    str1 = input("\nPlease enter a string: ")
                    encrypted_message = encrypt_string(str1)
                    print("\nThe encrypted message is:", encrypted_message)
                    
                else: #checks for number out of the range of 1-2 for string operations
                    print("You entered a number out of range. Please enter either 1 or 2.")

            except ValueError:
                print("Non-numerical character entered. Please enter either 1 or 2.")

        else: #checks for number out of range of 1-2 for original user option
            print("You entered a number out of range. Please enter either 1 or 2.")

    except ValueError:
        print("Non-numerical character entered. Please enter either 1 or 2.")

main()

                    
