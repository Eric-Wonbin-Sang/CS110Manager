#I pleadge my honro that I have abided by the Stevens Honor Code
#Number 2

def main():
    list_1 = input("Enter any amount of numbers sperated by a space:")
    list_of_sums = list_1.split()
    sum_num = 0
    for i in list_of_sums:
        sum_num += int(i)
    print(sum_num)
main()