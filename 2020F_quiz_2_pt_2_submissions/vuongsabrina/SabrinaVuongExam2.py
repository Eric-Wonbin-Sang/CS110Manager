#I pledge on my honor that I have abided by the Stevens Honor System.
#I understand that I may access the course textbook and course lecture notes but I am not to access any other resource. I also pledge that I worked alone on this exam.

def Add(n):
    return n[0]+n[1]

def Subtract(n):
    return n[0]-n[1]

def Multiply(n):
    return n[0]*n[1]

def Divide(n):
    return n[0]/n[1]

def Vowels(c3):
    num_vowels = 0
    for i in c3:
        if ((i=="a")|(i=="e")|(i=="i")|(i=="o")|(i=="u")):
            num_vowels+=1
    return num_vowels

def Encrypt(c3):
    newWord = ""
    increment = 1
    for i in c3:
        newWord+= str(ord(i)+increment)+" "
        increment+=1
    return newWord

def validNumber(c):
    validNum = False
    for i in c:
        decimalCount = 0
        invalidChars = 0
        for j in i:
            if (j == "."):
                decimalCount += 1
            elif ((j.isnumeric() == False)):
                invalidChars += 1
        if ((decimalCount > 1) | (invalidChars > 1)):
            validNum = True
        if ((invalidChars == 1) & (i[0:1] != "-")):
            validNum = True
    return validNum

def main():
    print("For Mathematical Functions, Please Enter the Number 1")
    print("For String Operations, Please Enter the Number 2")
    choice1 = str(input(""))
    while((choice1!="1") & (choice1!="2")):
        print("You did not enter a valid number choice. Please enter either 1 or 2.")
        choice1 = str(input(""))
    if(choice1=="1"):
        print("For Addition , Please Enter the Number 1")
        print("For Subtraction, Please Enter the Number 2")
        print("For Multiplication, Please Enter the Number 3")
        print("For Division, Please Enter the Number 4")
        choice2 = str(input(""))
        numEquation_unfiltered = []
        numEquation = []
        while((choice2<"1") | (choice2>"4")):
            print("Your choice input for which operation you want was not valid. Please enter a 1, 2, 3, or 4.")
            choice2 = str(input(""))

        print("Please enter the two numbers you want to evaluate, separated by a space.")
        while(len(numEquation)!=2):
            numEquation = []
            equation = str(input(""))
            while (equation == ""):
                print("You didn't enter any numbers. Please enter values to perform an operation on.")
                equation = str(input(""))
            numEquation_unfiltered = equation.split(" ")
            dontContinue = False
            for i in range(len(numEquation_unfiltered)):
                if(numEquation_unfiltered[i]!=""):
                    numEquation.append(numEquation_unfiltered[i])
            if (len(numEquation)!=2):
                print("You did not enter two values. Please try again.")

        dontContinue = validNumber(numEquation)

        if (dontContinue==False):
            for i in range(len(numEquation)):
                for j in numEquation[i]:
                    if ((j!=".") & (j!="-")):
                        if (j.isnumeric() == False):
                            print("You have failed to input valid numbers. Please restart the program.")
                            dontContinue = True
                            break
                if(dontContinue == False):
                    numEquation[i] = float(numEquation[i])
                else:
                    break
            if (dontContinue == False):
                if(choice2=="1"):
                    ans=Add(numEquation)
                    print("Adding these two numbers gives you", ans)
                elif(choice2=="2"):
                    ans=Subtract(numEquation)
                    print("Subtracting these two numbers gives you", ans)
                elif (choice2 == "3"):
                    ans=Multiply(numEquation)
                    print("Multiplying these two numbers gives you", ans)
                elif (choice2 == "4"):
                    while(numEquation[1]==0):
                        print("You cannot divide by 0. Please input a valid second value.")
                        numEquation[1]= str(input(""))
                        while (numEquation[1] == ""):
                            print("You didn't enter any numbers. Please enter values to perform an operation on.")
                            numEquation[1] = str(input(""))

                        decimalCount = 0
                        invalidChars = 0
                        for j in numEquation[1]:
                            if (j == "."):
                                decimalCount += 1
                            elif ((j.isnumeric() == False)):
                                invalidChars += 1
                        if ((decimalCount > 1) | (invalidChars > 1)):
                            dontContinue = True
                        if ((invalidChars == 1) & (numEquation[1][0:1] != "-")):
                            dontContinue = True

                        for j in numEquation[1]:
                            if ((j != ".") & (j != "-")):
                                if (j.isnumeric() == False):
                                    print("You have failed to input valid numbers. Please restart the program.")
                                    dontContinue = True
                                    break
                    if (dontContinue == False):
                        numEquation[1] = float(numEquation[1])

                    if (dontContinue == False):
                        ans=Divide(numEquation)
                        print("Dividing these two numbers gives you", ans)
        if (dontContinue):
            print("You have failed to input valid numbers. Please restart the program.")


    elif(choice1=="2"):
        print("To Determine the Number of Vowels in a String; Enter the Number 1")
        print("To Encrypt a String; Enter the Number 2")
        choice2 = str(input(""))
        while ((choice2 != "1") & (choice2 != "2")):
            print("You did not enter a valid number choice. Please enter either 1 or 2.")
            choice2 = str(input(""))
        print("Please input a string to evaluate")
        choice3 = str(input("")).lower()
        if (choice2=="1"):
            ans = Vowels(choice3)
            print("There are", ans, "vowels in '"+choice3+"'." )
        elif (choice2 == "2"):
            ans = Encrypt(choice3)
            print("Your encrypted message is ", ans)

main()