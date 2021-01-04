# I pledge my Honor that I have abided by the Stevens Honor System
# Maya Okrasinska

def main():
    print("This program is designed to open a file, change the format of the")
    print("strings in this file, and then write the reformatted strings into")
    print("a new file.")
    print()
    infileName = input("What file are the names currently in? ")
    outfileName = input("What file should the formatted names be then placed into? ")
    infile = open(infileName,"r")
    outfile = open(outfileName,"w")
    for i in infile:
        name = i.title()
        print(name, file = outfile)
    infile.close()
    outfile.close()
    print()
    print("The names have successfully been placed to:", outfileName)
main()

