Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #I pledge my honor that I have abided by the Stevens Honor System
>>> #this code gives the uder a list of menus to choose from
>>> def main():
	first = input("Enter 1 for mathematical fucntions, 2 for string fucntions. ")
	first = int(first)
	if first == 1:
		math = input("For additon enter 1, For subtraction enter 2, For multiplication enter 3, For division enter 4. ")
		math = int(math)
		if math == 1:
			A = float(input("Please enter the first number you would like: "))
			B = float(input("Please enter the second number you would like: "))
			sum = A+B
			print("The sum is:", sum)
		elif math == 2:
			C = float(input("Please enter the first number you would like to subtract, the second number will be subtracted from the first: "))
			D = float(input("Please enter the second number you would like to multiply: "))
			dif = C-D
			print("The difference is:", dif)
		elif math == 3:
			E = float(input("Please enter the first number that you would like to multiply, Please enter the second number you would like to multiply: "))
			F = float(input("Please enter the first number that you would like to multiply, Please enter the second number you would like to multiply: "))
			product = round(E*F, 4)
			print ("The answer is:", product)
		elif math == 4:
			G = float(input("Please enter the first number that you would like to divide (The first number will be divided by the second number): "))
			H = float(input("Please enter the second number that you would like to divide: "))
			quotient = round (G/H, 4)
			print("The answer is:", quotient)
		else:
			print("Error! please run program again and enter a number between 1 and 4.")
	elif start == 2:
		stringer = input("to determine the number of vowels in a string, enter the number 1. \to encrypt a string, enter the number 2.")
		stringer = int(stringer)
		if stringer == 1:
			string = input ("Enter the string: ")
			vowel1 = string.count("a")
			vowel2 = string.count("e")
			vowel3 = string.count("i")
			vowel4 = string.count("o")
			vowel5 = string.count("u")
			sum2 = vowel1 + vowel2 + vowel3 + vowel4 + vowel5
			print("There are", sum2, "vowels in the string.")
		elif stringer == 2:
			message = input ("enter the message you would like to encrypt: ")
			print("the encrypted message is: ")
			for i in message:
				x = ord(i)
				print(" ", x*x+x-2, end = "")
			else:
				print("Error! please run program again and enter the number 1 or 2.")
		else:
			print("Error! please run program again and enter the number 1 or 2.")

			
>>> main()
Enter 1 for mathematical fucntions, 2 for string fucntions. 1
For additon enter 1, For subtraction enter 2, For multiplication enter 3, For division enter 4. 2
Please enter the first number you would like to subtract, the second number will be subtracted from the first: 12
Please enter the second number you would like to multiply: 5
The difference is: 7.0
>>> 