
print("This program makes usernames")
print("from a file of names")

infileName = input("What file is it in? ")
outfileName = input("Place username in this file: ")

infile = open(infileName, "r")
outfile = open(outfileName, "w")

for i in infile:
    first, last = i.split()
    uname = (first + last).upper()
    print(uname, file=outfile)

infile.close()
outfile.close()
print("Usernames have been written to: ", outfileName)

