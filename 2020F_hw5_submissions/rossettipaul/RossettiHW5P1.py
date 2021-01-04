#I pledge my Honor that I have abided by the Stevens Honor System.
import math
def main():
    listt = eval(input("Enter a list of integers"))
    sqr(listt)
    print(listt)
def sqr(listx):
    for i in range(len(listx)):
        listx[i] = listx[i] * listx[i]

main()