#2020F_hw5_submissions problem 1
#I pledge my honor that I have abided by the Stevens honor system -Maya O

def main():
    def square(y):
        return [y**2 for y in x] 
    n = int(input("How many numbers would you like to square? "))
    x = []
    for i in range(0,n):
        list = float(input("Enter number: "))
        x.append(list)
    print("The given numbers squared are:", square(x))
main()


