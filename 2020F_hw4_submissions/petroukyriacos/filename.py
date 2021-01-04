def main():
        print("This program capitalizes names in a new text file ")
        infilename ='C:/Users/petro/Documents/CS 110/Before.txt'
        #Before.txt
        outfilename = 'C:/Users/petro/Documents/CS 110/After.txt'
        #After.txt
        infile = open(infilename, "r")
        outfile = open(outfilename, "w")
        for i in infile:
                capital = i.upper()
                print(capital, file=outfile)
        infile.close
        outfile.close
        print("The capitalized names are in the file: ", outfilename)

main()
