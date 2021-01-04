#I pledge my honor I had abided by the Stevens Honor System

#This program will open a .txt file and produce a new .txt file with the capitalized names

def main():
    print("This program generates a new .txt (After.txt) file with capitalized names")
    print("from an existing .txt file (Before.txt) of names.")

    infile = open("Before.txt", "r")
    outfile = open("After.txt", "w")

    for line in infile:
        capitalizedname = line.upper()
        print(capitalizedname, file=outfile)
    infile.close()
    outfile.close()

    print("The capitalized names have been")
    print("written to After.txt")

main()