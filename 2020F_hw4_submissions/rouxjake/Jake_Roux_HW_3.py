#I pledge my honor that I have abided by the Stevens Honor System.
#Jake Roux

def main():
    print("This program will pull names from a file.")
    print("Then it will capitalize them and put them in a new file")
    
    infileName = input("File containing names:")
    outfileName = input("Place capitalized names in this file:")
    
    for name in infile:
        CAPNAME = upper.name
        print(CAPNAME, file = outfile)
        
    infile.close()
    outfile.close()
    
    print("Capitalized names have been")
    print("Written to:", outfileName)

main()


