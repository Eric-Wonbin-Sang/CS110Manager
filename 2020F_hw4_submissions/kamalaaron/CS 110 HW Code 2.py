#Aaron Kamal- I Pledge my honor that I have abided by the stevens honor system

def main():
    print("This program capatilizes a list of names.")
    infilename=input("Enter the names of the file containing the names: ")
    #before.txt
    outfilename=input("Enter the name of the file containing the capatilized names: ")
    #after.txt
    infile = open(infilename, "r")
    outfile = open(outfilename, "w")
    for i in infile:
        capital = i.upper()
        print(capital, file=outfile)
    infile.close
    outfile.close
    print("The capatilized names are in: ",outfilename)
main()    
    
