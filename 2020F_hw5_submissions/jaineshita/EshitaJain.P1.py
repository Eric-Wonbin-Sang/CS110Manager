# square each entry in list
# I pledge my Honor that I have
# abided by the Stevens Honor System.

def square(num):
    for i in range(len(num)):
        num[i] = num[i] ** 2

def main():
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    square(num)
    print(num)
main()