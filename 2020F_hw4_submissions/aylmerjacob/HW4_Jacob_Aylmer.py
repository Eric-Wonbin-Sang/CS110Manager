# 2020F_hw4_submissions
# Jacob Aylmer

def main():
    print("this program makes names uppercases")
    print("from a file of lowercase names.\n")

    # get the file names
    infileName = input("what files are the lowercase names in?: ")
    outfileName = input("place uppercase names in this file: ")

    # open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file
    for i in infile:
        # get lowercase first and last names
        first, last = i.split()
        # upper name
        uname = (first+(" ")+last).upper()
        # write to output file
        print(uname, file=outfile)

    # close both files
    infile.close()
    outfile.close()

    print("uppercase names have been")
    print("written to:", outfileName)


main()
