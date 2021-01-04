# I, Michael Catania, agree to the Stevens Honor Code
# This program squares an input list of numbers
import math
def square():
    nums = input("Enter a list of nuimbers seperated by commas:")
    sqaured = []
    list = nums.split(",")
    for n in list:
        sqaured.append(int(n) ** 2)
    print(sqaured)
square()
