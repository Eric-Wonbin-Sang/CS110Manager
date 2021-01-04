# Square List / Sum List
# I pledge my honor that I have abided by the Stevens Honor System

"""
Inputs: The numbers/integers into a list
Process: Squaring each number/Adding the elements
Outputs: The new list/sum of the elements
"""


def list_modifier_one():
    list = []
    new_list= []
    i = input("How many numbers do you want to add to the list? ")
    for j in range(int(i)):
        k = input("Enter a number: ")
        list.append(k)
    print(list)
    for element in list:
        new_element = int(element) * int(element)
        new_list.append(new_element)
    print(new_list)
    print()

def list_modifier_two():
    list = []
    i = input("How many numbers do you want to add to the list? ")
    for j in range(int(i)):
        k = int(input("Enter a number: "))
        list.append(k)
    print(list)
    print("The sum of the elements is " + str(sum(list)))


list_modifier_one()
list_modifier_two()
