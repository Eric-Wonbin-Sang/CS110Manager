#I pledge on my honor that I have abided by the Stevens Honor System
import math
import csv
import os
import matplotlib.pyplot as plt


def sum(n):
    total = 0
    for i in range(len(n)):
        total+=n[i]
    return total

def main():
    chosen = str(input("Please enter your list of numbers, separated by commas"))
    numbers=[]
    numbers = chosen.split(",")
    for i in range(len(numbers)):
        numbers[i]=float(numbers[i])
    print("The sum of all these numbers", sum(numbers))
main()