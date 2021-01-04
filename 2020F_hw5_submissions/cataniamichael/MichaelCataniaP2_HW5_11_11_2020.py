# I, Michael Catania, agree to the Stevens Honor Code
# This program returns the sum of an input list
import math
def main():
    nums = input("Enter a list of numbers seperated by commas:")
    addition = []
    list = nums.split(",")
    for n in list:
        addition.append(int(n))
    print(sum(addition))
main()
    
