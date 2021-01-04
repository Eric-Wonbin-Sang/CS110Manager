#Sidharth Peri
#10/22/20
#Honor Code: i pledge in my honor that I have abided by the Stevens Honor System
#A program that opens a text file formats the strings and then writes
#the reformatted strings in a new text file

def main():
    print("This program takes a text file with lower case names and writes them into a new")
    print("text file with all uppercase letters")

    #get file names
    beforeFile = input("What is the name of the file? ")
    afterFile = input("Place names in this file: ")

    #open files
    before = open(beforeFile, 'r')
    after = open(afterFile, 'w')

    #for loop to split first and last name into separate strings and use upper function to
    #create a new string with uppercase names
    for i in before:
        first, last = i.split()
        new_name= first.upper() + " " + last.upper()
        print(new_name,file=after)

    #close files
    before.close()
    after.close()

    print("Names have been printed to", afterFile)

main()
