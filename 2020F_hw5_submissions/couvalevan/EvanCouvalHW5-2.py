def square(userList):
    for i in range(len(userList)):
        userList[i] = int(userList[i]) ** 2
    return userList

def main():
    userList = []
    x = (input("enter a list of numbers seperated by commas: "))
    userList = x.split(",")
    userList = square(userList)
    print(userList)
main()

