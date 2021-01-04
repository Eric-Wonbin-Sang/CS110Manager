#JoeRotundopy
#I pledge my honor that I have abided by the Stevens Honor System Joseph Rotundo

def main():
    print("This program will convert all lowercase text")
    print("to uppercase.")
    infileName = input("What file would you like to convert?: ")
    outfileName = input("Which file would you like to write the converted text in?: ")
    #open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")
    for i in infile:
        print(i.upper(), file=outfile)
    infile.close()
    outfile.close()
    print("The new text has been written to: ", outfileName)
main()
        
