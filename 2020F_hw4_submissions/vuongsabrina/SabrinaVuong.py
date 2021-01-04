#I pledge on my honor that I have abided by the Stevens Honor System
import math
import csv
import matplotlib.pyplot as plt

def main():
    infile = open("Before.txt", "r")
    outfile = open("After.txt", "w")
    for i in infile:
        print(i.upper(), file=outfile)
    infile.close()
    outfile.close()
    print("Usernames have been written to After.txt")

main()


