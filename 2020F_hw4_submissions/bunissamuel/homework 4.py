def main():
    print("This program changes the names in a file to all capital letters")
    infileName = input("What files are the names in? ")
    outfileName = input("Place names in this file: ")

    infileName = open(infileName, "r")
    outfileName = open(outfileName,"w")

    for line in infileName:
        line = line.upper()
        outfileName.write(line)
main()
