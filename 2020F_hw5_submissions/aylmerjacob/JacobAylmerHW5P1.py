# i pledge my honor i have abided by the stevens honor code

def main():
    n = int(input("how many items in the list? "))
    l = list(float(number) for number in input("enter elements of the list, separted by a space: ").strip().split())[:n]
    print("the elements in your list are: ", l)
    for i in range(n):
        l[i] = l[i] * l[i]
    print("each element squared is: ", l)

main()
