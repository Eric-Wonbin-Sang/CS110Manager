import math
def main():
   theSum = 0
   numbers = eval(input("Enter numbers seperated by commas: ")) 
   for i in numbers:
        theSum = theSum + i
   print("The sum is ", theSum)
main()
