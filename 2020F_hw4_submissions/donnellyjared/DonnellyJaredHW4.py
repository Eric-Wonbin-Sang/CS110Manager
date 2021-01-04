# By: Jared Donnelly
# CS 110 - Homework 4
# I pledge my Honor that I have abided by the Stevens Honor System

def assignUserName():
    # assigns files to be opened and either read or written into
    inputfile = open("Before.txt", "r")
    outputfile = open("After.txt", "w")

    # goes through each name in the file and capitalizes them before writing them into the outputfile
    for i in inputfile:
        output = i.upper()
        print(output, file=outputfile)

    # closes the files and declares to the user that the process is finished
    inputfile.close()
    outputfile.close()
    print("Usernames have been written to: After.txt")

# calls function to be run
assignUserName()
