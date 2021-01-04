def main():
    infile="Before.txt"
    outfile="After.txt"
    inputfile=open(infile, "r")
    outputfile=open(outfile, "w")
    for i in inputfile:
        x=i.upper()
        print(x,file=outputfile)
    inputfile.close()
    outputfile.close()
main()



        
