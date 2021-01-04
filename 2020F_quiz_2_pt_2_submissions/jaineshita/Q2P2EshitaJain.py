# I pledge my Honor that I have abided by the Stevens Honor System.
# I understand that I may access the course textbook and course lecture notes
# but I am not to access any other resource. I also pledge that I worked
# alone on this exam.
# Eshita Jain
# Quiz two Part two

def main():
    try:
        n = int(input("\nFor Mathematical Functions, Please Enter the Number 1. "
                  "\nFor String Operations, Please Enter the Number 2: "))
        if n == 1:
            m = int(input("\nFor Addition, Please Enter the Number 1."
                      "\nFor Subtraction, Please Enter the Number 2."
                      "\nFor Multiplication, Please Enter the Number 3."
                      "\nFor Division, Please Enter the Number 4: "))
            if m == 1:
                a = float(input("\nEnter the first number: "))
                b = float(input("Enter the second number: "))
                sum = a + b
                print("The sum is: ", sum)
            elif m == 2:
                a = float(input("\nEnter the first number: "))
                b = float(input("Enter the second number: "))
                diff = a - b
                print("The difference is: ", diff)
            elif m == 3:
                a = float(input("\nEnter the first number: "))
                b = float(input("Enter the second number: "))
                x = a * b
                print("The product is: ", x)
            elif m == 4:
                a = float(input("\nEnter the first number: "))
                b = float(input('Enter the second number: '))
                d = a / b
                print("The quotient is: ", d)
            else:
                print("\nError: User has entered an invalid entry.")
                main()

        elif n == 2:
            t = int(input("\nTo Determine the Number of Vowels in a String; Enter the Number 1. "
                      "\nTo Encrypt a String; Enter the Number 2: "))
            if t == 1:
                str = input("Enter a message: ")
                lowercase = str.lower()

                vowel_counts = {}

                for vowel in "aeiou":
                    count = lowercase.count(vowel)

                    vowel_counts[vowel] = count

                print(vowel_counts)
            elif t == 2:
                message = input("Enter message to encode: ")
                key = int(input("Enter an integer value for the key: "))
                print("The encrypted message is: ")
                for i in message:
                    print(ord(i) + key, end=' ')
            else:
                print("\nError: User has entered an invalid entry.")
                main()
        else:
            print("\nError: User has entered an invalid entry.")
            main()
    except ValueError:
        print("\nError: User has entered an invalid entry.")
        main()
main()