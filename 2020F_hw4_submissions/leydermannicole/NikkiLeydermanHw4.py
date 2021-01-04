# I pledge my honor that I have abided by the Stevens Honor System
def main():
    name=0
    infileName = input("What files are the names in?")
    outfileName = input("Place uppercase names in this file: ")
    infile=open(infileName, "r")
    outfile = open(outfileName, "w")
    for i in infile:
        n= i.title()
        print(n, file=outfile)
    infile.close()
    outfile.close()
main()