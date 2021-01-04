# By: Jared Donnelly
# CS 110 - Prof. Kevin Ryan
# I pledge my Honor that I have abided by the Stevens Honor System

def main():
    print("The following program accepts numerical inputs and squares them")
    print("Please list all the numbers you would like to enter in a list separated by spaces")
    squarables = input("Please being inputting your numbers below: \n")

    squarables = squarables.split()

    for num in range(len(squarables)):
        squarables[num] = int(squarables[num]) ** 2

    print("The inputted list squared is: \n", squarables)


main()
