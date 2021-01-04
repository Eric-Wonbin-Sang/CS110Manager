#I pledge my honor that I have abided by the Stevens Honor System. Jill McDonald
#This function will accept a list of numbers and square each element of the
#list.

def squarelist(lst):
    for i in range(len(lst)):
        lst[i]=lst[i]*lst[i]

def main():
    mylst=[0,1,2,3,4,5]
    squarelist(mylst)
    print(mylst)

main()
    
