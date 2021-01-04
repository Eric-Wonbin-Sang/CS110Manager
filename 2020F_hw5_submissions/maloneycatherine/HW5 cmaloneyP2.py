# Catherine Maloney - CS110 HW5
# I pledge my honor that I have abided by the Stevens honor system.

# Problem Two: Write and test a Python program which has a function which
# accepts a list of numbers and returns the sum of the numbers in the list.

def main():
    
    list1 = input("Enter a list of numbers separated by a space: ")
    sum_list = list1.split()
    sum1 = 0
    
    for i in sum_list:
        sum1 = sum1 + int(i)
    print("The sum of the list of numbers is:", sum1)
    
main()
