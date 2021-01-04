# I pledge my honor I have abided by the Stevens Honor code - Tyson Werner

def sum(numbers):
    summed_up = 0
    for i in numbers:
        summed_up = summed_up + float(i)
    return summed_up

def main():
    numbers = input("Enter a list of numbers separated by a space: ").split()
    print("The sum of your numbers is: ", sum(numbers))

main()
