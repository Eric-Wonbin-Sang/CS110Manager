#1
def numberlist():
    ui = input("Enter a list of numbers. Please put a space between each number ")
    List = list(int(num) for num in ui.strip().split())
    for i in range(len(List)):
        List[i] = List[i] ** 2
    print(List)
numberlist()

#2
def numberlist2():
    print("\n")
    ui2 = input("Enter a list of numbers. Please put a space between each number ")
    List2 = ui2.split()
    sum2 = 0
    for num in List2:
        sum2 += float(num)
    print("Sum = ", sum2)

numberlist2()
