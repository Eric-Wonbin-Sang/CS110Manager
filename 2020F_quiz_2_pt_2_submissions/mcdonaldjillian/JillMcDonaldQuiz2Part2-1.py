#I pledge my honor that I have abided by the Stevens Honor System. Jill McDonald
#I understand that I may access the course textbook and course lecture notes
#but I am not to access any other resource.
#I also pledge that I worked alone on this exam.
#Quiz 2 Part Two

def numbVowels(string):
    count = 0
    for letter in string:
        if letter in "AEIOUaeiou":
            count = count + 1

    print("There are " + str(count) + " vowels in " + string)


def encrypt(string):
    encrypted = ""
    for letter in string:
        if not letter.isalpha():
            encrypted = encrypted + letter
            continue
        
        unicode = ord(letter)
        if letter.isupper():
            index = unicode - ord("A")
            new_index = (index + 3) % 26
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            encrypted = encrypted + new_character
        else:
            index = unicode - ord("a")
            new_index = (index + 3) % 26
            new_unicode = new_index + ord("a")
            new_character = chr(new_unicode)
            encrypted = encrypted + new_character

    print("Encrypted string: " + encrypted)

def main():
    print("For Mathematical Functions, Please Enter the Number 1")
    print("For String Operations, Please Enter the Number 2")
    resp = input()
    if resp == "1":
        print("For Addition, Please Enter the Number 1")
        print("For Subtraction, Please Enter the Number 2")
        print("For Multiplication, Please Enter the Number 3")
        print("For Division, Please Enter the Number 4")
        resp = input()

        numb1 = float(input("Please enter the first number: "))
        numb2 = float(input("Please enter the second number: "))

        if resp == "1":
            print(numb1 + numb2)

        if resp == "2":
            print(numb1 - numb2)

        if resp == "3":
            print(numb1 * numb2)
            
        if resp == "4":
            print(numb1 / numb2)

    if resp == "2":
        print("To Determine the Number of Vowels in a String; Enter the Number 1")
        print("To Encrypt a String; Enter the Number 2")

        resp = input()

        string = input("Please enter a string: ")

        if resp == "1":
            numbVowels(string)

        if resp == "2":
            encrypt(string)


main()
