import math

def square():
    numbers = input("Enter the numbers in the list seperated by a comma: ")
    squared = []
    list = numbers.split(",")
    for number in list:
        squared.append(int(number) ** 2)
    print(squared)







square()