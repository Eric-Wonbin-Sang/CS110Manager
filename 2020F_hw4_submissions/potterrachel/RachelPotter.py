# RachelPotter.py
# A program that changes the lowercase names in a .txt file to uppercase and prints them to a new file

def main():
    infile_name = "Before.txt"
    outfile_name = "After.txt"
    infile = open(infile_name, "r")
    outfile = open(outfile_name, "w")
    for row in infile:
        for letter in row:
            cap_name = letter.capitalize()
            print(cap_name, end="", file=outfile)
    infile.close()
    outfile.close()
    print("Capitalized names have been written to:", outfile_name)


main()

# I pledge my honor that I have abided by the Stevens Honor System
# Rachel Potter
