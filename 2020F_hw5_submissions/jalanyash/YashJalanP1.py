# I pledge my honor that I have abided by the Stevens Honors System
import math
def main():
    size = int(input("How many numbers would you like to enter?"))
    myList = list(float(number)for number in input("Enter the list of numbers with spaces:").strip().split())[:size]
    print("the list is currently",myList)
    for x in range(size):
        myList[x]= myList[x] ** 2
    print ("the new list is",myList)
main()
