#I pledge my Honor that I have abided by the Stevens Honor System
#I understand that I may access the course textbook and course lecture notes
#but I am not to access any other resource. I also pledge that I worked alone on this exam.

#This program will ask you to select an item in a menu.
#The user will select a menu item, and the program will perform the chosen operation.

def main():
    print("For Mathematical Functions, Please Enter the Number 1")
    print("For String Operations, Please Enter the Number 2")
    FValue=int(input("Enter Number 1-2: "))
    if FValue == 1:
        print("You have chosen Mathematical Functions")
        print("For Addition, Please Enter the Number 1")
        print("For Subtraction, Please Enter the Number 2")
        print("For Multiplication, Please Enter the Number 3")
        print("For Division, Please Enter the Number 4")
        FSValue=int(input("Enter number 1-4: "))
        if FSValue == 1:
            print("You have chosen Addition")
            AValue = float(input("What is your first value: "))
            AValue2 = float(input("What is your second value: "))
            Addition = float(AValue) + float(AValue2)
            print(AValue, "+", AValue2, "=", round,(Addition,5))
        elif FSValue == 2:
            print("You have chosen Subtraction")
            SValue = float(input("What is your first value: "))
            SValue2 = float(input("What is your second value: "))
            Subtraction = float(SValue) - float(SValue2)
            print(SValue, "-", SValue2, "=", round(Subtraction,5))
        elif FSValue == 3:
            print("You have chosen Multiplication")
            MValue = float(input("What is your first value: "))
            MValue2 = float(input("What is your second value: "))
            Multiplication = float(MValue) * float(MValue2)
            print(MValue, "*", MValue2, "=", round(Multiplication,8))
        elif FSValue == 4:
            print("You have chosen Division")
            DValue = float(input("What is your first value: "))
            DValue2 = float(input("What is your second value: "))
            Division = float(DValue) / float(DValue2)
            print(DValue, "/", DValue2, "=", round(Division, 8))
        else:
            print("Error, invalid entry, please choose a whole number between 1-4")
    elif FValue == 2:
        print("You have chosen String Operations")
        print("To Determine the Number of Vowels in a String; Enter the Number 1")
        print("To Encrypt a String; Enter the Number 2")
        SSValue=int(input("Enter a number 1-2: "))
        if SSValue == 1:
            print("You have chosen to determine the number of vowels in a String")
            VString = input("Enter the string you would like to determine the number of vowels in: ")
            Vowels = 0
            for i in VString:
                if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
                        or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
                    Vowels = Vowels + 1
            print("The number of vowels in your string is", Vowels)
        elif SSValue == 2:
            Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            def shift(shifting):
                EString = input("Enter the string you would like to encrypt: ")
                Encryption = ''
                for ch in EString:
                    if ch.isalpha():
                        new_pos = Alphabet.index(ch) + shifting
                        new_shift = Alphabet[new_pos]
                        Encryption += new_shift
                    elif ch in ' \t\n':
                        Encryption += ch
                    elif ch.isnumeric():
                        Encryption += ch
                    else:
                        print("An error took place in encrypting the string. Use alphabet only.")
                print(Encryption)
            shift(-3)
        else:
            print("Error, invalid entry, please choose a whole number between 1-2")
    else:
        print("Error, invalid entry, please choose a whole number between 1-2")
main()