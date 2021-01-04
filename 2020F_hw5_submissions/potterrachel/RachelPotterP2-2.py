# RachelPotterP2.py
# A program that takes a list of numbers and returns the sum of numbers in the list

def list_sum(num_list):
    total_num = 0
    for i in range(len(num_list)):
        total_num = total_num + num_list[i]
    return total_num


# Let's test it!
# We can create a function to get a list from the user to pass through list_sum(num_list)
# then print the results so we can see.
def get_list():
    num_list = []
    num_string = input("Enter a list of numbers to be added, separated by a comma: ")
    for num in num_string.split(","):
        num = float(num)
        num_list.append(num)
    print(list_sum(num_list))  # Call our adding function and print the return


get_list()

# I pledge my honor that I have abided by the Stevens Honor System
# Rachel Potter
