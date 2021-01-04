#I pledge my honor that I have abided by the Stevens Honor System
#Jeffrey Eng

def main():
    infile = open("Before.txt", "r")
    outfile = open("After.txt", "w")
    for i in infile:
        x = i.upper()
        print(x, end="", file = outfile)
    infile.close()
    outfile.close()
main()
