#I pledge my honor I had abided by the Stevens Honor System
#This program will produce the sum of a user inputted list

def main():
    print("This program will provide the sum of a list of numbers.")
    input_string = input("Enter a list of numbers separated by space: ")
    UserList = input_string.split()
    print("Your list is ", UserList)
    sum = 0
    for numbers in UserList:
        sum += int(numbers)
    print("The sum of your list is = ", sum)
main()
