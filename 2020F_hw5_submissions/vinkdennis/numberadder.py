#this program accepts a list of numbers
#then takes the list and adds all the values together 
#I pledge my honor that I have abided by the Stevens Honor System

def main():
    print("This program accepts a list of numbers and adds them")
    x = []
    numbers = int(input("Enter the amount of numbers you have: "))
    for i in range(numbers):
        sums = int(input("Enter a number: "))
        x.append(sums)
    
    print("The sum of numbers is: ", sum(x)) 
    print("Have a great day!")
main()
