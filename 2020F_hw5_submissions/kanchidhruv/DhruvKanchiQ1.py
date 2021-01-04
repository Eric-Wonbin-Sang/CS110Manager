# I pledge my honor that I have abided by the Stevens Honor System.

def main():
    x = int(input("What size would you like the list to be?"))
    lst = list(float(number) for number in input("Please enter the elements you would like to include in your list, and separate each element with a space.").strip().split())[:x]
    print("The elements you entered for your list are", lst)
    for i in range(x):
        lst[i] = lst[i] ** 2
    print("Each element of your list squared is", lst)
		
main()
