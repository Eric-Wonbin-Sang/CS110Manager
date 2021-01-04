#this program accepts a list of numbers
#then takes the list and sqaures each value 
#I pledge my honor that I have abided by the Stevens Honor System

def main():
    print("This program accepts a list of numbers and squares them")
    x = 0
    numbers = int(input("Enter the amount of numbers you have: "))
    for i in range(numbers):
        square = int(input("Enter a number: "))
        squared = (square*square)
        print("The value squared is ", squared)
    print("Have a great day!")
main()
        
    
    
