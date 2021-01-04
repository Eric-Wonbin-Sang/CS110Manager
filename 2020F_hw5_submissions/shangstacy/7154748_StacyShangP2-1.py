# StacyShangP2.py
# CS 110 A HW 5
# Stacy Shang
# I pledge my honor that I have abided by the Stevens Honor System -Stacy

# This program accepts a list of numbers and squares each entry

usernum_string = input("Enter a list of numbers with each separated by a space: ")
usernum_list_string = usernum_string.split(' ')

List1 = []
for n in usernum_list_string:
  List1.append(int(n))
sumList1 = sum(List1)

print("Original numbers:\n",List1)
print("Sum of numbers:\n", sumList1)
