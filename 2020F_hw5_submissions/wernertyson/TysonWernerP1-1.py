#I pledge my honor I have abided by the Stevens Honor code - Tyson Werner

def squaring(numbers):
    return [float(i) * float(i) for i in numbers]

def main():

    numbers = input("Enter a list of numbers separated by a space").split()
    print(squaring(numbers))

main()
