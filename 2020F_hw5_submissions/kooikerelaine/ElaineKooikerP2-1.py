#Homework 5
#ElaineKooikerP2
#I pledge my honor that I have abided by the Stevens Honor Code.

#Write and test a Python program which has a function
#which accepts a list of numbers and returns the sum of the numbers in the list.

def sum(numbers):
    sum=0
    for i in range (len(numbers)):
       sum=sum+numbers[i]
    return sum

def main():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list=sum(list)
    print(list)
main()
