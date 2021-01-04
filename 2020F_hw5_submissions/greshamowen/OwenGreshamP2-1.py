# I pledge my honor that I have abided by the Stevens Honor System - Owen Gresham

def sum_list(nums):
    total = 0
    for i in nums:
        total += i
    return total


def main():
    print("This program takes a list of numbers and prints the sum")
    nums = input("Enter a sequence of numbers separated by commas: ").split(",")
    for i in range(len(nums)):
        nums[i] = float(nums[i])
    sum = sum_list(nums)
    print("The sum is", sum)


main()
