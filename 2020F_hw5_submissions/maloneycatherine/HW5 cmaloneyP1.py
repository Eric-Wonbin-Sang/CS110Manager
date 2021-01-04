# Catherine Maloney - CS110 HW5
# I pledge my honor that I have abided by the Stevens honor system.

# Problem One: Write and test a Python program which has a function
# which accepts a list of numbers and modifies the list by squaring each entry.

def main():
    
    list1 = input("Enter a list of numbers separated by a space: ")
    split_list = list1.split()
    list2 = []
    
    for square in split_list:
        list2.append(int(square) ** 2)

    print("The square of each number in this list is:", list2)
    
main()
