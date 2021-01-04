#I pledge my honor that I have abided by the stevens honor system.
#OmP2.py

def main():
    input_string = input("Enter a list of numbers separated by spaces ")
    x = input_string.split()
    print("The list entered is", x)
    sum = 0
    for i in x:
        sum += float(i)
    print("The sum of the numbers in the list is", sum)
main()
