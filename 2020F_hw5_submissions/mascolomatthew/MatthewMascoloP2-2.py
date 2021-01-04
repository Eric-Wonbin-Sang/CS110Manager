#MatthewMascoloP2.py
#I pledge my honor that I have abided
#by the Stevens Honor System. Matthew Mascolo
#
#Returns The Sum Of Integers In A List


def sumList(numList):
    listSum = 0
    
    for num in numList:
        listSum = listSum + num
        
    return listSum
    
def main():
    
    inFile = 'firstList.txt'
    outFile = 'sumList.txt'
    inFile = open(inFile, "r")
    outFile = open(outFile, "w")
    
    numList = []
    for i in inFile:
        num = int(i)
        numList.append(num)

    listSum = sumList(numList)
    
    print('Sum of List:', listSum, file=outFile)

main()
    
