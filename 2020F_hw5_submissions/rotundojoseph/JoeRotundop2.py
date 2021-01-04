#I pledge my honor that I have abided by the Stevens Honor System Joseph Rotundo

def main():
    results = eval(input("Enter the results you would like to take the sum of, separated by commas: "))
    sum=0
    for i in results:
        sum+= int(i)
    print(sum)
main()
