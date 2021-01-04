#Sidharth Peri
#HW 5 Question 2
#Honor Code: I pledge in my honor that I have abided by the Stevens Honor System

#A program that uses a function to accept a list and returns an integer that is the sum of the elements in the list

#function that takes in a list and an integer for the sum of the list as parameters
def sum_list(num_list, sum_elements):
    sum_elements = 0 #initializes local sum variable
    for i in range(len(num_list)):
        sum_elements = sum_elements + num_list[i]
    return sum_elements #must return sum variable because it is an integer

#main function in which function call occurs
def main():
    num_list = [1,2,3,4,5,6] #initialize list
    sum_of_numbers = 0 #initialize sum variable in main function
    sum_of_numbers = sum_list(num_list, sum_of_numbers) #call function, must reassign sum_numbers variable to function call as integers are immutable
    print("The sum of the elements in the list is:", sum_of_numbers)

main()
