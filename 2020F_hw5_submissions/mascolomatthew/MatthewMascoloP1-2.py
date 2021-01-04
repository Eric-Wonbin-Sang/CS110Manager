#MatthewMascoloP1.py
#I pledge my honor that I have abided
#by the Stevens Honor System. Matthew Mascolo
#
#Squaring Integers Of A List

def square(numList):

    counter = 0
    for i in numList:
        numList[counter] = int(i) * int(i)
        counter = counter+1
    return numList
        
def main():
    inFile = 'beforeNums.txt'
    outFile = 'afterNums.txt'

    inFile = open(inFile, "r")
    outFile = open(outFile, "w")
    
    numList = []
    for i in inFile:
        num = int(i)
        numList.append(num)
    print(numList)
        
    print("List Before Square Function:", numList, file=outFile)
    numList = square(numList)
    print("List After Square Function:", numList, file=outFile)

    inFile.close()
    outFile.close()
    
main()
