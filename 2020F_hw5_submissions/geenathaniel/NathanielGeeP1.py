#I pledge my honor that I have abided by the Stevens Honor System. Nathaniel Gee

print("This program accepts a list of numbers and modifies the list by squaring each entry")

def square_the_number_list(numbers_list):
    for n in range(len(numbers_list)):
        numbers_list[n] = numbers_list[n] ** 2
    return numbers


response = input("Enter the number of entries:  ")
number_of_inputs = int(response)

numbers = []
for n in range(number_of_inputs):
    user_input = input("Enter a number:  ")
    numbers.append(int(user_input))

print("Original list of numbers: " + str(numbers))
new_numbers = square_the_number_list(numbers)
print("Squared list of numbers: "+ str(new_numbers))


