# I pledge my honor that I have abided by the Stevens Honor System.
# Melissa Atmaca

def square(list):
    for i in range(len(list)):
        list[i]= int(list[i]) ** 2
    print(list)
def main():
    input_num = input("Enter a number list separated by a comma: ")
    inputList = input_num.split(",")
    print("The new list is", end=" ")
    square(inputList)
main()


