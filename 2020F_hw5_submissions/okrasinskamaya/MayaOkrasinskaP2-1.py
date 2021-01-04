#2020F_hw5_submissions problem 2
#I pledge my honor that I have abided by the Stevens honor system -Maya O

def main():
    def sum(num):
        total = 0
        for y in num:
            total = total + y
        return total
    n = int(input("How many numbers would you like to add together? "))
    x = []
    for i in range(0,n):
        list = float(input("Enter number: "))
        x.append(list)
    print("The sum of the given numbers is:", sum(x))
main()
