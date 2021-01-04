# This program will open a .txt file, change the format of the strings in this file
# and then write the reformatted strings into a new .txt file

def main():
    print("This program converts an all lower case text file to all capital letters")
    input= open('Before.txt',"r")
    output= open('After.txt', "w")

    for i in input:
        uppercase=i.upper()
        print(uppercase, file=output)

    input.close()
    output.close()
    print("The lowercase names have been converted to uppercase")
    print("and written into After.txt")
main()