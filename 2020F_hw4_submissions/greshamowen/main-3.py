# I pledge my honor that I have abided by the Stevens Honor System - Owen Gresham
def main():
    infile = open("Before.txt", "r")
    outfile = open("After.txt", "w")
    for i in range(10):
        line = infile.readline().upper()
        print(line, file=outfile, end="")
    infile.close()
    outfile.close()
main()