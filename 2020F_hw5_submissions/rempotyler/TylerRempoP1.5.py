#I pledge my honor I had abided by the Stevens Honor System
# A program for squaring a list of User inputted numbers

def squareEach(Userlist):
   for i in range(len(Userlist)):
       Userlist[i] = Userlist[i] ** 2
   return Userlist
def main():
    print("This program will square a list of numbers.")
    input_string = input("Enter a list of numbers separated by space: ")
    Userlist = input_string.split()
    print("Your list is ", Userlist)
    for i in range(len(Userlist)):
        Userlist[i] = float(Userlist[i])
    squared_list= squareEach(Userlist)
    print("\nYour squared list is")
    print(squared_list)
main()



