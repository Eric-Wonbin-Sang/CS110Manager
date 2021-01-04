# i pledge my honor that i have abided by the stevens honor system- rachel flynn

def main():
    print("This program will convert the uncapitalized names to capitalized names")

    infileName=input("What file are the names in?: ")
    outfileName= input("Place new names in this file: ")

    infile=open(infileName,"r")
    outfile=open(outfileName,"w")

    for i in infile:
        first,last=i.split()
        newfirst=first[0:].upper()
        newlast=last[0:].upper()
        newname=" ".join([newfirst,newlast])
        print(newname,file=outfile)

    infile.close()
    outfile.close()

    print("New names have been written to:",outfileName)

main()
