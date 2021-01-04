#I pledge my honor that I have abided by the Steven's Honor System
#Ben Otto

#Write and test a Python program which has a function which
# accepts a list of numbers and modifies the list by squaring each entry.

def main():
    list=[]
    list=(input("Insert a list of numbers, seperated by only a comma").split(","))
    list2=[]
    for i in range(len(list)):
        list2.append(int(list[i])**2)
    return(list2)
main()