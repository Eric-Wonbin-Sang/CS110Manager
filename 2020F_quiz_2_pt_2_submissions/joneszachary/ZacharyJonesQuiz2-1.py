#Pledge: I pledge my Honor that I have abided by the Stevens Honor System
#I understand that I may access the course textbook and course lecture notes but I am not to access any other resource. I also pledge that I worked alone on this exam.

def select_menu():
    print('For Mathematical Functions, Please Enter the Number 1\n'
          'For String Operations, Please Enter the Number 2')

    try:
        select = int(input('Enter Selection: '))
        if select not in range(1, 3):
            print('Error: Invalid User Input')
        else:
            if select == 1:
                select_math()
            else:
                select_string()
    except:
        print('Error: Invalid User Input')


def select_math():
    print('For Addition, Please Enter the Number 1\n'
          'For Subtraction, Please Enter the Number 2\n'
          'For Multiplication, Please Enter the Number 3\n'
          'For Division, Please Enter the Number 4')
    select = int(input('Enter Selection: '))

    if select not in range(1, 5):
        print('Error: Invalid User Input')
    else:
        num1 = float(input('Enter Number 1: '))
        num2 = float(input('Enter Number 2: '))
        if select == 1:
            print(num1 + num2)
        elif select == 2:
             print(num1 - num2)
        elif select == 3:
             print(num1 * num2)
        else:
             print(num1 / num2)

def select_string():
    print('To Determine the Number of Vowels in a String: Enter the Number 1\n'
          'To Encrypt a String: Enter the Number 2')
    select = int(input('Enter Selection: '))

    if select not in range(1, 3):
        print('Error: Invalid User Input')
    else:
        string = str(input('Enter String: '))

        if select == 1:
            vowels_list = ['a', 'e', 'i', 'o', 'u']
            vowel_count = 0
            for char in string.lower():
                for vowel in vowels_list:
                    if char == vowel:
                        vowel_count += 1
            print(str(vowel_count) + ' vowels')

        else:
            ord_list = []
            encrypted_string = ''
            for char in string:
                ord_list.append(ord(char) + 1)

            for num in ord_list:
                encrypted_string += chr(num)
            print(encrypted_string)


select_menu()