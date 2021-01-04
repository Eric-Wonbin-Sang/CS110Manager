# I pledge my honor I have abided by the Stevens honor system
# Accepts a list of numbers and returns the sum of the numbers in the list

def summation(lst):
    return sum(lst)


def main():
    lst = []
    n = int(input("Enter the number of values to be summed: "))
    for i in range(n):
        lst.append(int(input("Enter value individual value: ")))
    print("The sum of the list elements is", summation(lst))


main()
