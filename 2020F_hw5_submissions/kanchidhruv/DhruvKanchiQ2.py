# I pledge my honor that I have abided by the Stevens Honor System.

def main():
    stringInput = input("Enter the numbers you would like to add separated by space.")
    lst = stringInput.split()
    print("The elements you entered for your list are", lst)
    sum1 = 0
    for number in lst:
        sum1 += float(number)
    print("The sum of all of of the elements in your list is", sum1)
		
main()
