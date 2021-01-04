# i pledge my honor i have abided by the stevens honor code

def main():
    string_input = input("enter numbers you want to add, separated by a space: ")
    l = string_input.split()
    print("the elements you entered are: ", l)
    sum = 0
    for number in l:
        sum += float(number)
    print("the sum of the elements of the list is: ", sum)

main()
