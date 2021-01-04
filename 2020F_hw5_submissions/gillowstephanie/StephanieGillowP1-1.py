# Stephanie Gillow
# I pledge my honor I have abided by the Stevens honor system.
# CS 110 HW 5
# 11/11/2020

def squareList(inList):
    outList = []
    for i in range(0, len(inList)):
        outList.append(float(inList[i]) * float(inList[i]))
    print(outList)
