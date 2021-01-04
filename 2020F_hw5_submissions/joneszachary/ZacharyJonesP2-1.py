#I pledge my honor that I have abided by the Stevens Honor System.
#Zachary Jones
#HW 5 Problem 2

def recursive_sum(list):
    if not list:
        return 0
    return list[0] + recursive_sum(list[1:])

number_list = [2, 4, 6, 10, 23, 432, 43, 782]

print('Sum of list: ' + str(recursive_sum(number_list)))