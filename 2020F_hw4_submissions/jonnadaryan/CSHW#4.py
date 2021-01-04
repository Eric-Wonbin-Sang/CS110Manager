#I pledge my honor that I have abided by the Stevens Honor System

def main():
    print ("This program capitalizes a list of names.")
    infilename = input("Enter the name of the file containing the names: ")
    # Before.txt
    outfilename = input("Enter the name of the file containing the capitalized names: ")
    # After.txt
    infile = open(infilename, "r")
    outfile = open(outfilename, "w")
    for i in infile:
        capital = i.upper()
        print(capital, file=outfile)
    infile.close
    outfile.close
    print("The capitalized names are in the file: ",outfilename)
main()
