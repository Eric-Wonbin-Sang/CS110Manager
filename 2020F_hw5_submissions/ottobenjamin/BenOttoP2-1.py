#I pledge my honor that I have abided by the Stevens Honor System
#Ben Otto

#Write and test a Python program which has a function
# which accepts a list of numbers and returns the sum of the numbers in the list.

def main():
    list=(input("Input a list of numbers seperated by only commas").split(","))
    sum=0
    for i in range(len(list)):
        list[i]=int(list[i])
        sum+=list[i]
    return(sum)
main()