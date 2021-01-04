#HW5P1
#By: Jacob Buurman
#I pledge my honor that I have abided by the Stevens Honor System.

def square():
    list = eval(input("Enter a list of numbers separated by commas: "))
    square_list = [i ** 2 for i in list]
    print(square_list)

square()
