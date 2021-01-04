input_string = input("Enter list of numbers, make sure to put a space after each number")

userNumbers = input_string.split()
sum1 = 0
for num in userNumbers:
    sum1 += int(num)
print("The sum of the numbers in the list is", sum1)