#I pledge my honor that I have abided by the Stevens Honor System.
#This program accepts a list of numbers and returns their sum.

def sumlst(lst):
    result=0
    for i in range(len(lst)):
        result=result+lst[i]

    return result

def main():
    mylst=[0,1,2,3,4,5]
    result=sumlst(mylst)
    print(result)

main()
