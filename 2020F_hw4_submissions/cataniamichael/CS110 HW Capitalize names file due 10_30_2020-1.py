# This Program Converts names from lowercase to capital letters
def main():
    print("This program converts names from lowercase to capital letters")
    infileName = input("What file are the names in? ")
    outfileName = input("Place names with all uperecase letters in this file: ")
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")
    for i in infile:
        cap = (i.upper())
        print(cap, file=outfile)
    infile.close()
    outfile.close()
    print("The capitalized names are in:", outfileName)
main()
    
