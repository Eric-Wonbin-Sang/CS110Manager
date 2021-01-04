def main():
 infileName = input("What are the names in?:")

 outfileName = input("Place usernames in this file:")

 infile = open(infileName, "r")

 outfile = open(outfileName, "w")

 for i in infile:
    first, last = i.split()
    uname = (first + ' ' + last).upper()
    print(uname, file= outfile)

 infile.close()
 outfile.close()

 print("Usernames have been written to:", outfileName)

main()
    
    
