#I pledge my honor that I have abided by the Stevens Honor System.
#Zachary Jones
# HW 5 Problem 1

def recursive_square(list):
    if not list:
        return []
    return [list[0] ** 2] + recursive_square(list[1:])


numbers_list = [2, 4, 6, 8, 10, 11]

print('Squared entries: ' + str(recursive_square(numbers_list)))
