#I pledge my honor to abide by the Stevens Honor Code
#Kayla Batzer HW 4

def main():

    beforetxt = open("C:/Users/Kayla/Desktop/CS 110/before.txt", "r")
    aftertxt = open("after.txt", "w")

    for string in beforetxt:
        after = string.upper()
        print(after, end = "")
        aftertxt.write(after)
    open("after.txt", "r")

main()