#I pledge my honor that I have abided by the stevens honor code

def main():
    numbers = eval(input("Enter the numbers you would like to take the sum of seperated by commas: "))
    sum = 0
    for i in numbers:
        sum+=int(i)
    print(sum)
main()
