def squares(list):
    for i in range(len(list)):
        list[i] = int(list[i]) ** 2
    print(list)
def main():
    input_list = input("Enter values separated by a space: ")
    list = input_list.split()
    print(list)
    squares(list)
    print("the new list is: ", list)

main()
