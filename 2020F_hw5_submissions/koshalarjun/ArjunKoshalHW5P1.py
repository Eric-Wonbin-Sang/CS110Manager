# This is Arjun Koshal's Homework 5 Problem 1 Solution
# I pledge my honor that I have abided by the Stevens Honor System
# This program will accept a list of numbers and modifies the list
# by squaring each entry

def main():
    n = int(input("Enter the size of the list "))
    numList = list(float(num) for num in input("Enter a list of elements separated by space ").strip().split())[:n]
    print("The entries of the list are", numList)
    for i in range(n):
        numList[i] = numList[i] ** 2
    print("The entries of the list squared are", numList)

main()

