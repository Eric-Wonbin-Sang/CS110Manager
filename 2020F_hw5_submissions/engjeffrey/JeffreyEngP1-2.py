# I pledge my honor that I have abided by the Stevens Honor System.
# Jeffrey Eng

def square3(p):
    for i in range(len(p)):
        p[i] = float(p[i])**2
    return p

def main():
    numbers = input("Enter a list of numbers separated by spaces: ")
    x = numbers.split()
    print("The squares are", square3(x))
main()
