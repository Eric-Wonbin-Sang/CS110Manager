#Kayla Batzer
#HW 5 P2
#I pledge my honor to abide by the Stevens honor code

def listsum(list):
    sumNum = 0
    for i in list:
        sumNum = sumNum + i
    return sumNum

def main():
    numList = [1, 2, 3, 4, 5]
    numList = listsum(numList)
    print(numList)
main()
