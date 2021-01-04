import math
def main():
    results = eval(input("Entet the results you would like to take the sum of and separate them by commas:"))
    sum=0
    for i in results:
        sum+= int(i)
    print(sum)
main()
