# I pledge my honor that I have abided by the Stevens Honor System.
# Melissa Atmaca

def add(list):
    sum = 0
    for i in range(len(list)):
        sum += int(list[i])
    print(sum)
def main():
    input_num = input("Enter a number list separated by a comma: ")
    inputList = input_num.split(",")
    print("The sum is", end=" ")
    add(inputList)
main()
