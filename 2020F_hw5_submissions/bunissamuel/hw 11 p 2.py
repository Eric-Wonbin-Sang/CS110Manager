import math

def main():
    numbers = input("Enter the numbers in the list seperated by a comma: ")
    addition = []
    list = numbers.split(",")
    for number in list:
        addition.append(int(number))
    print(sum(addition))

main()