#I pledge my Honor that I have abided by the Stevens Honor System.
import math
def main():
    listt = eval(input("Enter a list of integers"))
    summ = sqr(listt)
    print(summ)
def sqr(listx):
    sum = 0
    for i in range(len(listx)):
        sum += listx[i]
    return sum
main()