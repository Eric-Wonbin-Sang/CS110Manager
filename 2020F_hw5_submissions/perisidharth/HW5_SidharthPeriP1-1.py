#Sidharth Peri
#HW 5 Question 1
#Honor Code: I pledge in my honor that I have abided by the Stevens Honor System

#A program that uses a function to accept a list and returns a modified list with the elements squared

#function that takes in a list as a parameter and returns the list with each element squared
def square_list(squared_list):
    for i in range(len(squared_list)):
        squared_list[i] = squared_list[i]**2 #no need for return because lists are mutable
        
#main function in which function call occurs
def main():
    num_list = [1,2,3,4,5,6]
    square_list(num_list) #call function, no need to reassign num_list because lists are mutable
    print("The squared list is:", num_list)

main()
