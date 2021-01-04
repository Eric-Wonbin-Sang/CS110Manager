# This program capitalizes ten names in an external file

def main():
    print("This program capitalizes lists of names in files")

    sourcefile = input("What is the name of the file with the list of uncapitalized names?: ")

    read = open(sourcefile, "r")
    write = open("After.txt", "w+")

    for i in read:
        capp = i.title()
        print(capp, file=write)

    read.close()
    write.close()
main()