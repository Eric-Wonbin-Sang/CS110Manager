#I pledge my honor that I've abided by the Stevens Honor System - Nicholas DiGiacomo
def sume(numbers,):
    numbers3 = sum(numbers)
    return numbers3

def main():
    numbers2 = []
    input_numbers = int(input("Enter the number of values:"))
    for i in range(0, input_numbers): 
        x = int(input("Enter the number:")) 
        numbers2.append(x) 
    numbers3 = sume(numbers2)  
    print("Here's the old list:",numbers2)
    print("Here's the sum of the list:",numbers3)
main()
