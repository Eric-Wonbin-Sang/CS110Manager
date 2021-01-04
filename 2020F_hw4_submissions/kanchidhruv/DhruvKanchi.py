# I pledge that I have abided by the Stevens Honor Code.

def main():
    print("This program will capitalize the letters of all the names in the Before file and store the capitalized names in the After file") 
    inFile = open('Before.txt', "r")
    outFile = open('After.txt', "w")
    for line in inFile:
        data = line.upper()
        print(data, file=outFile)
    inFile.close()
    outFile.close()
main()
