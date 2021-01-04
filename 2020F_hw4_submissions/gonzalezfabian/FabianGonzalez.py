#FabianGonzalez.py

#I pledge my honor that I have abided by the Stevens Honor System. Fabian Gonzalez.

def main():
    print("This program converts all lowercase text to all uppercase text.")
    infileName= input("Which file would you like to convert into uppercase text?:")
    outfileName= input("In Which file would you like to write the converted text in?:")
    infile= open(infileName, "r")
    outfile=open(outfileName, "w")
    for i in infile:
        print()
        print(i.upper())
    infile.close()
    outfile.close()
    print("The converted, uppercase text has been written to "+outfileName)
    print()
main()

input('Press ENTER to exit')