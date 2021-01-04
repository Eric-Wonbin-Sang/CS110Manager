# I, Alvin Radoncic, abide by the Stevens Honor Code
# Problem 2, Homework 5
# This program accepts a list of numbers and returns the sum of the numbers.

def summed_list():

    number_of_terms = int(input("How many numbers do you want to list? "))
    sum = 0

    for i in range(number_of_terms):
        x = float(input("Enter any number: "))
        sum = sum + x
        print("The current sum is", sum)

    print()
    print("The sum of all inputted numbers is: " + str(sum))

summed_list()
