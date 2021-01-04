#MatthewMascolo.py
#I pledge my honor that I have abided
#by the Stevens Honor System. Matthew Mascolo
#
#This program takes a list of New York Knicks players
#and staff in Before.txt, then it capitalizes all
#players' first and last names and prints them out in After.txt
def main():
    
    inFile = 'Before.txt'
    outFile = 'After.txt'

    inFile = open(inFile, "r")
    outFile = open(outFile, "w")
  
    for i in inFile:
        first, last = i.split()
        newName = first.upper() + " " + last.upper()
        print(newName, file=outFile)

    inFile.close()
    outFile.close()
    
main()
