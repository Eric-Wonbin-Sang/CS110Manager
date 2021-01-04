# Pledge: I pledge my Honor that I  abide by the Stevens Honor System

def sumValues():

    userNumberList = []
    l = int(input("How many numbers are in the list? "))
    total = 0
    for i in range(1,l+1):
        print("Enter Number", i)
        numholder = int(input())
        total += numholder
        userNumberList.append(numholder)
    print("\n")
    print("This is your original list of numbers entered into the function: ", userNumberList)
    print("The sum of the numbers: ", total)


def main():

    sumValues()

main()