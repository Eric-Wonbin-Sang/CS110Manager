# I pledge my honor that I have abided by the Stevens Honor System - Owen Gresham

def square_list(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2
    return nums


def main():
    print("This program takes a sequence of numbers and squares each number")
    nums = input("Enter a sequence of numbers separated by commas: ").split(",")
    for i in range(len(nums)):
        nums[i] = float(nums[i])
    squared_list = square_list(nums)
    print("\nThe list of squared numbers:")
    print(squared_list)


main()
