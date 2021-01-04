# I pledge my honor that I have abided by the Stevens Honor Code
# Riley Sikorski

#This program will accept a list of numbers
#It will square the numbers

def main():
    print("This program will accept a list of numbers and squares them all. ")
    list = []
    n = eval(input("Please enter the number of numbers in your list:"))
    for i in range(0 , n):
        item = eval(input("Enter the number:"))
        list.append(item)
    print("The original list is", list)

    listNew = []
    for i in range(0,n):
        i = list[i]*list[i]
        listNew.append(i)
    print("The squared list is", listNew)

main()
