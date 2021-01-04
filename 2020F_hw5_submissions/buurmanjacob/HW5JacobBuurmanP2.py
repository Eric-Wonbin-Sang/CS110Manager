#HW5P2
#By: Jacob Buurman
#I pledge my honor that I have abided by the Stevens Honor System.

def sum():
    list = eval(input("Enter a list of numbers separated by commas: "))
    sum = 0
    for num in list:
        sum += int(num)
    print(sum)

sum()
