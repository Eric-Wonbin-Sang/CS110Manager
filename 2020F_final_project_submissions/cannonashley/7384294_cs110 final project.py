import math
def encrypt(password):
    result = []
    for character in password:
        l = ord(character)**2 + 25
        result.append(l)
    print("This is your encrypted password!")
    for numbers in result:
        print(numbers, end='')
        print(" ", end = '')
    print()
    decrypt(result)
    
def decrypt(result):
    end_string = ""
    for numbers in result:
        l = int(numbers)
        l = int(math.sqrt(l - 25))
        l = chr(l)
        end_string = end_string + l
    print("Your decrypted password is: ")
    print(end_string)


def main():
    password = input("Enter your password: ")
    encrypt(password)
main()
