Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #I pledge my honor that I have abided by the Stevens Honor System -Kyriacos Petrou
>>> #valid date code
>>> def main():
	date = input("Enter the date in mm/dd/2001 format: ")
	month, day, year = date.split('/')
	month=int(month)
	day=int(day)
	year=int(year)
	if month == 4 or month == 6 or month == 9 or month == 11:
		if 1<= day <= 30 and year > 0:
			print("Date is valid. ")
		else:
			print("Date is invalid. ")
	if month  == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
		if 1 <= day <= 31 and year > 0:
			print("Date is valid. ")
		else:
			print("Date is invalid. ")
	if month == 2:
		if 1 <= day <= 28 and year > 0:
			print("Date is valid. ")
		else:
			print("Date is invalid. ")

			
>>> main()
Enter the date in mm/dd/2001 format: 9/7/2001
Date is valid. 
>>> 