# I, Alvin Radoncic, abide by the Stevens Honor Code
# Problem 1, Homework 5
# This program accepts a list of numbers and modifies it by squaring each entry

def squared_list():

    number_of_terms = int(input("How many numbers do you want to square? "))
    square = []

    for i in range(number_of_terms):
        number = float(input("Enter a number: "))
        x = number * number
        square.append(x)

    print(square)

squared_list()

