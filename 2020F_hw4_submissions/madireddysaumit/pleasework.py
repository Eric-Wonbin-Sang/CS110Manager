#I pledge my honor that I have abided by the Stevens Honor System

def main():
    infile = open('before.txt', "r")
    outfile = open('after.txt', "w")
    for line in infile:
        data = line.title()
        print(data, file=outfile)
    infile.close()
    outfile.close()
main()
