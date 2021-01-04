#Homework 5
#ElaineKooikerP1
#I pledge my honor that I have abided by the Stevens Honor Code.


# Write and test a Python program which has a function
#which accepts a list of numbers and modifies the list by squaring each entry.

def square(numbers):
    for i in range (len(numbers)):
        numbers[i]=numbers[i]**2
    return numbers

def main():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list=square(list)
    print (list)
main()
