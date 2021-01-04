# By: Jared Donnelly
# CS 110 - Prof. Kevin Ryan
# I pledge my Honor that I have abided by the Stevens Honor System

def main():
    print("The following program accepts numerical inputs and sums them")
    print("Please list all the numbers you would like to enter in a list separated by spaces")
    sumables = input("Please being inputting your numbers below, then hit enter when you're finished: \n")
    finalSum = 0

    sumables = sumables.split()

    for num in range(len(sumables)):
        finalSum = finalSum + int(sumables[num])

    print("The total sum of the list is:", finalSum)


main()
