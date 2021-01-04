#I pledge my honor that I have abided by the Stevens Honor System. Jill McDonald
#This program reads Before.txt line by line and then converts each line to upper
#case letters, and writes each line into the After.txt file.

def main():
    fd = open("Before.txt", "r")
    fw = open("After.txt", "w")

    for line in fd:
        
        line = line.upper()
        fw.write(line)

    fd.close()
    fw.close()

    fd = open("After.txt", "r")
    print(fd.read())
    fd.close()

main()
