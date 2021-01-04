Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #I pledge my honor that I have abided by the Stevens Honor system -Kyriacos Petrou
>>> #write a program that computes the sum of a list of numbers
>>> def main():
	lst = []
	num = int(input('How many numbers: '))
	for n in range(num):
		numbers = int(input('Enter number '))
		lst.append(numbers)
	print("Sum of elements in given lists is :", sum(lst))

	
>>> main()
How many numbers: 5
Enter number 1
Enter number 2
Enter number 3
Enter number 4
Enter number 5
Sum of elements in given lists is : 15
>>> 