#I pledge my honor that I've abided by the Stevens Honor System - Nicholas DiGiacomo
import math

def squared(numbers):
    for i in range(len(numbers)):
        numbers[i]=numbers[i]**2
    return numbers

def main():
    numbers2 = []
    input_numbers = int(input("Enter the number of values:"))
    for i in range(0, input_numbers): 
        x = int(input("Enter the number:")) 
        numbers2.append(x) 
      
    print("Here's the old list:",numbers2)

    numbers_squared = squared(numbers2)
    print("Here's the new list:",numbers_squared)

main()
    
    

    
    
