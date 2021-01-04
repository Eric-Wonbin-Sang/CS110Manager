#I pledge my honor that I have abided by the stevens honor system.
#OmP1.py

def main():
    n = int(input("How many numbers would you like in the list?"))
    numlist = list(float(x) for x in input("Enter a list of numbers separated by spaces.").strip().split())[:n]
    print("The entries of the list are", numlist)
    for i in range(n):
        numlist[i] = numlist[i] ** 2
    print("Each of these values squared is", numlist)
main()
    
