#Homework 4
#I pledge my Honor that I have abided by the Stevens Honor Code. Elaine Kooiker

def main():
    print ("This program capitalizes a list of names")
    print("from a file of names.\n")

    #open the file
    beforeList = open("Before.txt", "r") #read
    afterList = open("After.txt", "w")    #write
    
    #process each line of input file
    for i in beforeList:
        i = i.upper()
        print(i, file=afterList)
        
    #close both files
    beforeList.close()
    afterList.close()
    print("Names have been written to \"After\" ")
   


main()
