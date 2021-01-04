#StepanyanP1.py
#I pledge my honor that I have abided by the Stevens Honor System
# This program squares an input list of numbers

def summation():
    User_Input = input("Input numbers separated by spaces: ")
    list = User_Input.split()

    newlist = [int(i) for i in list]

    for i in range(0, len(newlist)):
        newlist[i] = newlist[i]*newlist[i]

    print(newlist)
summation()