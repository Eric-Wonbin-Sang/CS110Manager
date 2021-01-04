# I pledge my honor I have abided by the Stevens honor system
# Accepts a list of numbers and modifies the list by squaring each entry

def recursive_square(list_of_numbers):
    # Base Case
    if not list_of_numbers:
        return []
    # Recursive Call
    return [list_of_numbers[0] ** 2] + recursive_square(list_of_numbers[1:])


def main():
    list_of_numbers = []
    n = int(input("Enter the number of values: "))
    for i in range(n):
        list_of_numbers.append(int(input("Enter value individual value: ")))
    print("The new list with squared elements is: ", recursive_square(list_of_numbers))


main()
