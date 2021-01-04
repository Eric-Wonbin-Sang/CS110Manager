# I pledge my Honor that I have abided by the Stevens Honor System.
# Melissa Atmaca 

def main():

    iName = input("What folder are the names in? ")
    oName = input("Place capitalized names in this file: ")

    infile = open(iName, "r")
    outfile = open(oName, "w")

    for i in infile:
        cname = i.upper()
        print(cname, file=outfile)

    infile.close()
    outfile.close()
    print("Capitalized names have been")
    print("written to:", oName)

main()
