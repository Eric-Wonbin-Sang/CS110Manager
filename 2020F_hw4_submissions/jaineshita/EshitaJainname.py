# I pledge my Honor that I have
# abided by the Stevens Honors System.
# Eshita Jain

def main():
    print("This program changes names")
    print("from a lowercase letters to uppercase letters.\n")
    infileName = input("What files are the names in? ")
    outfileName = input("Place uppercase names in this file: ")
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    for i in infile:
        first, last = i.split()
        capital = (first + " " + last).upper()
        print(capital, file=outfile)
    infile.close()
    outfile.close()
    print("Capital names have been written to: ", outfileName)
main()