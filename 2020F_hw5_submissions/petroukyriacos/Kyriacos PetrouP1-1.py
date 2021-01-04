Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #I pledge my honor that I have abided by the Stevens Honor system
>>> #Question 1:Squaring a list of numbers
>>> def main():
	numbers = [1, 2, 3, 4, 5]
	squared_numbers = [number ** 2 for number in numbers]
	print(squared_numbers)

	
>>> main()
[1, 4, 9, 16, 25]
>>> 