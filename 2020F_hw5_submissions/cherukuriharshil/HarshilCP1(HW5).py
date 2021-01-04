# Pledge: I pledge my Honor that I  abide by the Stevens Honor System

def squareValues():

    userNumberList = []
    squaredNumberList = []
    l = int(input("How many numbers are in the list? "))
    for i in range(1,l+1):
        print("Enter Number",i)
        numholder = int(input())
        newholder = numholder ** 2
        userNumberList.append(numholder)
        squaredNumberList.append(newholder)
    print("\n")
    print("This is your original list of numbers entered into the function: ", userNumberList)
    print("This is your modified list of numbers: ", squaredNumberList)


def main():

    squareValues()

main()