def listsum(numbers):
    sum = 0
    for i in numbers:
        sum += int(i)
    return sum
def main():
    input_string = input("Enter values separated by a space: ")
    numbers = input_string.split()
    print(numbers)
    listsum(numbers)
    print(listsum(numbers))
    print("the sum of the list is", listsum(numbers))
main()
