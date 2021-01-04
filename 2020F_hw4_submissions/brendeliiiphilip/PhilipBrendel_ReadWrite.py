#Philip Brendel
#I pledge my honor that I have followed the Stevens Honor code

file = "/Users/pjbrendel/Desktop/CS 110/Before.txt"
file2 = "/Users/pjbrendel/Desktop/CS 110/After.txt"

inputfile = open(file, "r")
outputfile = open(file2, "w")
for i in inputfile:
    upper = i.upper()
    print(upper, file = outputfile, end = '')
inputfile.close()
outputfile.close()
