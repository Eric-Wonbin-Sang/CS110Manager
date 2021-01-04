input_string = input("Enter list of numbers, make sure to put a space after each number")

userNumbers = input_string.split()

sqr = []
for i in userNumbers:
    if i.isdigit():
        num = int(i)
        sqr.append(num**2)
print("The square of each number in the list is ", sqr)
