#I pledge on my honor that I have abided by the Stevens Honor System
import math
import csv
import os
import matplotlib.pyplot as plt


def square(n):
    for i in range(len(n)):
        n[i]=n[i]**2
    return n

def main():
    chosen = str(input("Please enter your list of numbers, separated by commas"))
    numbers=[]
    numbers = chosen.split(",")
    for i in range(len(numbers)):
        numbers[i]=float(numbers[i])
    newnumbers = square(numbers)
    print("Your new numbers are",newnumbers)
main()