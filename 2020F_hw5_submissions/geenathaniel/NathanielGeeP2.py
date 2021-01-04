#I pledge my honor that I have abided by the Stevens Honor System. Nathaniel Gee

print("This program accepts a list of numbers and returns the sum of the numbers in the list.")

def add_numbers_in_list(numbers_list):
    sum = 0
    for n in range(0, len(numbers_list)):
        sum += numbers_list[n]
    return sum

response = input("Enter the number of entries:  ")
number_of_inputs = int(response)

numbers = []
for n in range(number_of_inputs):
    user_input = input("Enter a number:  ")
    numbers.append(int(user_input))

print("Original list of numbers:" + str(numbers))
sum_of_numbers = add_numbers_in_list(numbers)
print("The sum of the list of numbers:" + str(sum_of_numbers))