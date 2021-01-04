# I pledge my honor that I have abided by the Stevens Honor System
# Ashley Cannon

def main():
    print("This program generates usernames from a file of names. \n")
    infilename = input("What files are the names in: ")
    outfilename = input("Place names in this file: ")
    infile = open(infilename, "r")
    outfile = open(outfilename, "w")
    for i in infile:
        first, last = i.split()
        names = (first[0:], last[0:]).upper()
        print(names, file = outfile)
    infile.close()
    outfile.close()
    print("Names have been written to:", oufilename)

main()

