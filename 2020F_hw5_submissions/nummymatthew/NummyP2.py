#################################################################################
# Name       : Matthew Nummy
# Date       : 11/11/2020
# Assignment : Homework 5 - Part 2
# Pledge     : I pledge my honor that I have abided by the Stevens Honor System.
#################################################################################
def main():
    n = input("Enter the number of elements in your list: ")
    n = int(n)
    lst = []
    for i in range(n):
        if i == 0:
            m = int(input("Enter the first element of your list: "))
            lst.append(m)
        elif i > 0 and i < n - 1:
            m = int(input("Enter the next element of your list: "))
            lst.append(m)
        else:
            m = int(input("Enter the last element of your list: "))
            lst.append(m)
    print(sum(lst))


main()