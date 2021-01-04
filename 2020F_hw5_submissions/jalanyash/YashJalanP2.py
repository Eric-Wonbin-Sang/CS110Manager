# I pledge my honor that I have abided by the Stevens Honors System
def main():
    listinput= input("Enter numbers that you would like to be added with a space:")
    myList=listinput.split()
    print("the current list is", myList)
    sum=0
    for x in myList:
        sum+=float(x)
    print("the sum of the numbers in your list is", sum)
main()