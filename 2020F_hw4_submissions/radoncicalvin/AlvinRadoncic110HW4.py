
# I, Alvin Radoncic, abide by the Stevens Honor Code.

def main():
    print("This program capitalizes all of the first and last names in a given txt file.\n")

    #Establishing initial file name, Before, and the After file.
    Initial_File_Name = input("State the name of the file. (In this demo, it is Before.txt) \n")
    Capital_File_Name = input("Name the file where the capitalized names will be. (In this assignment, it is After.txt) \n")

    # Opening the files
    BeforeFile = open(Initial_File_Name, "r")
    AfterFile = open(Capital_File_Name, "w")

    for i in BeforeFile:
        first, last = i.split()
        capitalized = (first + " " + last).upper()
        print(capitalized, file=AfterFile)
    BeforeFile.close()
    AfterFile.close()

    print()
    print("The names have been capitalized, and are now placed into:", Capital_File_Name)
main()

