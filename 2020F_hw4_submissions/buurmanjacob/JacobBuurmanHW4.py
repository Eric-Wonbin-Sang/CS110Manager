#HW4
#By: Jacob Buurman
#I pledge my honor that I have abided by the Stevens Honor System.

def main():
    print("This program will open a .txt file (Before.txt) with a list of 10 lowercase names, capitalize")
    print("every uncapitalized letter, and then write the result in a new .txt file (After.txt).\n")
    #manually entered a list of 10 names in a .txt file and named it Before.txt
    infileName = input("What files are the names in? ")
    outfileName = input("Place usernames in this file: ")
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")
    for i in infile:
        first, last = i.split()
        uname = (first + " " + last).upper()
        print(uname, file = outfile)
    infile.close()
    outfile.close()
    print("Usernames have been written to:", outfileName)
main()
