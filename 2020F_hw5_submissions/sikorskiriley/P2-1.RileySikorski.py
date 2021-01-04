# I pledge my honor that I have abided by the Stevens Honor Code
# Riley Sikorski

#This program will accept a list of numbers
#It will return the sum of the numbers in the list 

def main():
    print("This program will accept a list of numbers and squares them all. ")
    list = []
    n = eval(input("Please enter the number of numbers in your list:"))
    for i in range(0 , n):
        item = eval(input("Enter the number:"))
        list.append(item)
    print("The list is", list)

    sum = 0
    for i in range(0,n):
        sum = sum + list[i]
    print("The sum of the elements in the list is ", sum)

main()
