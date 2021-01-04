# i pledge my honor that i have abided by the stevens honor system

def sumoflst(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return sum

#testing of function
def main():
    numbers = [1,2,3,4,5]
    print(sumoflst(numbers))
main()
