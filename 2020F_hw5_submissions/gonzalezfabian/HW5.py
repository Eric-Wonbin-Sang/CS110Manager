print("")
print("This function will ask you to input a list of numbers and then the function will square the numbers.")
print("")
squarerootinput = input("Enter the numbers you would like to square, and separate them with commas:").split(",")
print("")
list1= []
list2= []
for n in squarerootinput:
    list1.append(int(n))
for n in squarerootinput:
    list2.append(int(n)*int(n))
print("Input:", list1)
print("Output:", list2)
print("")
print("This function will ask you to input a list of numbers and then the function will add the numbers.")
print("")
input('Press ENTER to exit')