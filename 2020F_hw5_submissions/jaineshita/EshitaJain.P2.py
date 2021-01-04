# sum numbers in list
# I pledge my Honor that I have
# abided by the Stevens Honor System

def sumlist(num):
    sum = 0
    for n in num:
        sum = sum + n
    return sum

def main():
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sumlist(num))
main()