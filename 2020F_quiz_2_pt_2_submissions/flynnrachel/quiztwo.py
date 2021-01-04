#I pledge my Honor that I have abided by the Stevens Honor Sytstem. I understand that I may access the course textbook and course lecture notes but I am not to access any other
#resource. I also pledge that I worked alone on this exam.--Rachel Flynn
def main():
        try:
                print("""
                1.For Mathmatical Functions, Please Enter 1
                2.For String Operations, Please Enter 2
                """)
                askquestion= int(input("Enter number: "))
                if askquestion == 1:
                        print("""
                1. For Addition, Please Enter 1
                2. For Subtraction, Please Enter 2
                3. For Multiplication, Please Enter 3
                4. For Division, Please Enter 4
                        """)
                        try:
                                secondquestion = int(input("Enter number: "))
                                if secondquestion == 1:
                                        x = int(input("Enter first number: "))
                                        y = int(input("Enter second number: "))
                                        sum = x + y
                                        print(sum)           
                                elif secondquestion == 2:
                                        x = int(input("Enter first number: "))
                                        y = int(input("Enter second number: "))
                                        sub = x - y
                                        print(sub)
                                elif secondquestion == 3:
                                        x = int(input("Enter first number: "))
                                        y = int(input("Enter second number: "))
                                        product = x * y
                                        print(product)
                                elif secondquestion == 4:
                                        x = int(input("Enter first number: "))
                                        y = int(input("Enter second number: "))
                                        div = x / y
                                        print(div)
                                else:
                                        print("Error:Invalid Number")
                        except ValueError:
                                        print("Error:Non-numerical Character")
                elif askquestion == 2:
                        print("""
                1. To Determine the Number of Vowels in a String; Please Enter 1
                2. To Encrypt a String; Please Enter 2
                        """)
                        try:
                                thirdquestion = int(input("Enter a number: "))
                                if thirdquestion == 1:
                                        vowel = ["a","e","i","o","u","A","E","I","O","U"]
                                        string = (input("Please Enter a String: "))
                                        count = 0
                                        for i in string:
                                                if i in vowel:
                                                        count = count + 1
                                        print(count)
                                elif thirdquestion == 2:
                                        string = (input("Please Enter a String: "))
                                        for i in string:
                                                x = ord(i)
                                                print("",x+10,end = "")
                                else:
                                        print("Error:Invalid Number")
                        except ValueError:
                                print("Error:Non-numerical Character")
                else:
                        print("Error:Invalid Number")
        except ValueError:
                print("Error:Non-numerical Character")
                
main()
