# I pledge my honor that I have abided by the Stevens Honor System.
# Jeffrey Eng

def sum(p):
    total = 0
    for i in p:
        total += float(i)
    return total

def main():
    numbers = input("Enter a list of numbers separated by spaces: ")
    x = numbers.split()
    print("The sum is", sum(x))
main()
