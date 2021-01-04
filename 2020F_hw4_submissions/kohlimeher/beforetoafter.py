def main():
    print("This programs generates usernames from a file of names")
    infilename = input("Which file has all the names: ")
    outfilename =  input("Place usernames in this file: ")
    infile = open(infilename, "r")
    outfile = open(outfilename, "w")
    for i in infile:
        uname = i.upper()
        print(uname, file = outfile)
    infile.close()
    outfile.close()
    print("These usernames have been written in:", outfilename)
main()
