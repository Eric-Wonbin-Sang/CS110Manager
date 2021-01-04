#StepanyanP2.py
#I pledge my honor that I have abided by the Stevens Honor System
# This program finds the sum of a list of numbers

def squarefun():
    User_Input = input("Input numbers separated by spaces: ")
    list = User_Input.split()

    newlist = [int(i) for i in list]

    sum = 0

    for i in range(0, len(newlist)):
        sum = newlist[i] + sum

    print(sum)
squarefun()