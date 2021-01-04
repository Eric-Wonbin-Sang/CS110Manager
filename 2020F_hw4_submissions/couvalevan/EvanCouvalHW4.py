def main():

    fname = input("enter file name: ")
    infile = open(fname, "r")
    outfile = open("After.txt", "w")
    for line in infile.readlines():
        print(line.upper(), file=outfile , end="")
    infile.close()
    outfile.close()

main()