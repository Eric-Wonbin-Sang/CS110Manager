# StacyShangP1.py
# CS 110 A HW 5
# Stacy Shang
# I pledge my honor that I have abided by the Stevens Honor System -Stacy

# This program accepts a list of numbers and squares each entry

def square(List2):
  List1 = []
  for n in List2:
    List1.append(n**2)
  return(List1)

usernum_string = input("Enter a list of numbers with each separated by a space: ")
usernum_list_string = usernum_string.split(' ')

List3 = []
for n in usernum_list_string:
  List3.append(int(n)) 

print("Original numbers:\n",List3)
print("Squared numbers:\n", square(List3))
