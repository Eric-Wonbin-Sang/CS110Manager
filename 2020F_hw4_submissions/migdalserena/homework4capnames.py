# i pledge my honor that i have abided by the stevens honor system

def main():
    print("this program capitalizes a list of names")
    infilename = input("enter the name of the file containing names: ")
    outfilenames = input("enter the name of  the file containing the capitalized names: ")
    infile = open(infilename, "r")
    outfile = open(outfilenames, "w")
    for i in infile:
        cap = i.upper()
        print(cap, file=outfile)
    infile.close
    outfile.close
    print("the capitalized names are in the file: ", outfilenames)
main()
