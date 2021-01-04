def main():
    fname = input("Enter file name: ")
    inputfile = open(fname, "r")
    for line in open(fname):
        print(line.upper(), end='')

main()