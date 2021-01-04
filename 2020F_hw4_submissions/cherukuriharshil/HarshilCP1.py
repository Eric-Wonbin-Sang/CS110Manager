def main():

    # I pledge my honor that I have abided by the Stevens Honor System.

    infile = open('Before.txt', "r")
    outfile = open('After.txt', "w")
    for line in infile:
        line.upper()
        outfile.write(line.upper())

    infile.close
    outfile.close

main()
