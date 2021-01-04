# This is Arjun Koshal's Homework 5 Problem 2 Solution
# I pledge my honor that I have abided by the Stevens Honor System
# This program will accept a list of numbers and will then find the sum

def main():
    input_string = input("Enter a list of elements separated by space ")
    List = input_string.split()
    print("The entries of the list are", List)
    sum = 0
    for num in List:
        sum += float(num)
    print("The sum of the entries of the list are", sum)

main()