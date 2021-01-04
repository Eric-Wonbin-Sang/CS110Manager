# I pledge my honor I have abided by the Stevens honor system

def main():
    print("This program capitalizes the first letters of the first and last names.\n")
    print("The input file is Before.txt and the output file is After.txt.\n")
    infile = open("Before.txt", "r")
    outfile = open("After.txt", "w")
    for i in infile:
        export = i.upper()
        print(export)
        print(export, file=outfile)
    infile.close()
    outfile.close()
    print("New names have been written to After.txt")


main()
