# This assignment requests that you develop a Python program which will open a .txt file
# change the format of the strings in this file
# then write the reformatted strings into a new .txt file
# I pledge my honor that I have abided by the Stevens Honors System. Gabrielle Armetta

def main():
    print("This program opens a .txt file")
    print("and capitalizes all names in the file")
    # get the file names
    before = input()
    after = input()
    inputBefore = open(before, "r")
    inputAfter = open(after, "w")
    print(inputBefore.read().upper(), file=inputAfter)
    inputBefore.close()
    inputAfter.close()
main()