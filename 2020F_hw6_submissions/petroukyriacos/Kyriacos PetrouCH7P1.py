Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #I pledge my honor that I have abided by the Stevens Honor System -Kyriacos Petrou
>>> def main():
	# input the user
	height = float(input("Enter height in inches: "))
	weight = float(input("Enter weight in pounds: "))
	#formula to calculate BMI
	BMI = weight/(height**2)
	if (BMI < 19):
		print("under healthy range")
	elif(BMI >=19 and BMI < 25):
		print("healthy range")
	elif(BMI >=25):
		print("Above healthy range")

		
>>> main()
Enter height in inches: 71
Enter weight in pounds: 160
under healthy range 
>>> 
