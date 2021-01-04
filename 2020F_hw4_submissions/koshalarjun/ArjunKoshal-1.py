#This program will open a txt file, read the file, and create a new file


def main():
    infile = open('Before.txt', "r")
    outfile = open('After.txt', "w")
    for line in infile:
        data = line.upper()
        print(data, file=outfile)
    infile.close()
    outfile.close()
main()