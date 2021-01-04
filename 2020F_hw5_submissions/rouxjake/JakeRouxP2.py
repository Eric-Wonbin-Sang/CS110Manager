#I pledge my honor that I have abided by the Stevens Honor System. Jake Roux
def main():
    print("This program will return the sum of numbers you enter")
    num=eval(input("Separated by commas, enter your numbers:"))
    sum=0
    for i in num:
        sum+= int(i)
    print(sum)
main()

