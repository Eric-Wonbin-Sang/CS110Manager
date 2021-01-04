#I pledge my honor that I have abided by the Stevens Honor system
#This code is for Quiz 2, Part 2
#It will present the user with options

def main():
    print("This program will give you a few options in performing operations ")
    print("The first being within the scopes of a mathematical operation")
    print("The second being within the scopes of a string operation")

    x = int(input("If you have a math operation enter 1:, if you have a string operation enter 2: "))

        
    

    if x == 1:
        number = int(input("For addition enter: 1, subtraction: 2, multiplication: 3, division: 4 "))

        if number == 1:
                addition1 = int(input("Enter first number, must be integer: "))
                addition2 = int(input("Enter second number, must be integer: "))

                addition3 = addition1 + addition2

                print(addition3)

        elif number == 2:
                sub1 = int(input("Enter first number, must be integer: "))
                sub2 = int(input("Enter second number, must be integer: "))

                sub3 = sub1 - sub2

                print(sub3)

        elif number == 3:
                mult1 = int(input("Enter first number, must be integer: "))
                mult2 = int(input("Enter second number, must be integer: "))

                mult3 = mult1 * mult2

                print(mult3)

        elif number == 4:
                div1 = int(input("Enter first number, must be integer: "))
                div2 = int(input("Enter second number, must be integer: "))

                div3 = div1 / div2

                print(div3)

        else:
                print("ERROR: Incorrect value")

    elif x == 2:
       stri = int(input("Enter 1 to know the vowel count, enter 2 to encrypt the string: "))

       if stri == 1:
           stri1 = input("Enter the string:" )
           vowels = 'aieouAIEOU'
           count = 0 
        
           for j in stri1:
               if j in vowels:
                   count = count +1

           print("The amount of vowels in the string:", count)
            
       elif stri == 2:
           stri2 = input("Enter the string:")
           for i in stri2:
               x = ord(i)
               print("", x/5, end = "")

       else:
           print("ERROR: Incorrect value")
           
    
    else:
        print("ERROR: Incorrect value")
       
     
main()

    



    
