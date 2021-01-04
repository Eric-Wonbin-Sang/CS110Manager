# NameCap.py
# CS 110 A HW 4
# Stacy Shang
# I pledge my honor that I have abided by the Stevens Honor System -Stacy

# This program will open a .txt file, change the format of the strings
# in the file by changing the ten names in the .txt file to all have
# capital letters, then write the reformatted strings into a new .txt file
# The .txt files will be Before.txt and After.txt

def main():
    inputfileN = input("Enter a 'before' filename:")

    inputfile = open(inputfileN, "r")
    outputfile = open("After.txt", "w")

    for line in inputfile:
        outputfile.write(line.title())
        caps = line.title()
        print(caps)

    inputfile.close()
    outputfile.close()
main()
