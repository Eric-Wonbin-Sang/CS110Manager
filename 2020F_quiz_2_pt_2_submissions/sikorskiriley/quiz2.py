# I pledge my honor that I have abided by the Stevens Honor System
# I understand that I may access the course textbook and course lecture notes
# but I am not to access any other resource. I also pledge that I worked alone
# on this exam. 
def main():
    function = eval(input("For Mathematical Functions, Please Enter the Number 1.\nFor String Operations, Please Enter the Number 2."))
    if function == 1:
        number1 = eval(input("For Addition, Please enter the Number 1.\nFor Subtraction, Please Enter the Number 2.\nFor Multiplication, Please Enter the Number3.\nFor Division, Please Enter the Number 4."))
        digit1 = eval(input("Please enter the first number:"))
        digit2 = eval(input("Please enter the second number:"))
        total = 0; 
        if number1 == 1:
            total = digit1 + digit2
            print("The total is", total)
        elif number1 == 2:
            total = digit1 - digit2
            print("The total is", total)
        elif number1 == 3:
            total = digit1 * digit2
            print("The total is", total)
        elif number1 == 4:
            total = digit1 / digit2
            print("The total is", total)
        elif number1 < 1:
            print("Error. The number entered is not a valid option.")
        elif number1 > 4:
            print("Error. The number entered is not a valid option.") 
    elif function == 2:
        number2 = eval(input("To Determine the Number of Vowels in a String; Enter the Number 1.\nTo Encrypt a String; Enter the Number 2."))
        string = input("Please enter a string of letters:")
        if number2 == 1:
            vowel = 0
            for i in range (0, len(string)):
                if string[i] == "a":
                    vowel = vowel + 1
                elif string[i] == "e":
                    vowel = vowel + 1
                elif string[i] == "i":
                    vowel = vowel + 1
                elif string[i] == "o":
                    vowel = vowel + 1
                elif string[i] == "u":
                    vowel = vowel + 1
                else: 
                    vowel = vowel + 0
            print("The are", vowel, " vowels in the string.") 
        elif number2 == 2:
            d = round(len(string)/2)  
            left = string[0:d]
            right = string[d:]
            newString = right+left
            print("The encrypted string is: ", newString)  
        elif number2 < 1:
            print("Error. The number entered is not a valid option.")
        elif number2 > 2:
            print("Error. The number entered is not a valid option.") 
    elif function < 1:
        print("Error. The number entered is not a valid option.")
    elif function > 2:
        print("Error. The number entered is not a valid option.") 
main() 
