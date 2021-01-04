# RachelPotterP1.py
# A program that takes a list of numbers and modifies the list by squaring each entry

def square(num_list):  # Where num_list is a list
    for i in range(len(num_list)):
        num_list[i] = num_list[i]**2
    return num_list


# Let's test it!
# We can create a function to get a list input from the user to pass
# through square(), and then print the results so we can see.
def get_list():
    num_list = []
    num_string = input("Enter a list of numbers to be squared, separated by a comma: ")
    for num in num_string.split(","):
        num = float(num)
        num_list.append(num)
    square(num_list)  # Calling our square() function
    print(num_list)


get_list()

# I pledge my honor that I have abided by the Stevens Honor System
# Rachel Potter
