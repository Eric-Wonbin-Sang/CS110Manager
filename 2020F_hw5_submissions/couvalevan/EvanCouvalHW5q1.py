def add(userList):
    total = 0
    for i in range(0, len(userList)):
        total = total + int(userList[i])
    userList = total

    return userList

def main():
    userList = []
    x = (input("enter a list of numbers seperated by commas: "))
    userList = x.split(",")
    userList = add(userList)
    print(userList)


main()