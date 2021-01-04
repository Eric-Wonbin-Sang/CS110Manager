# I pledge my honor that I have abided by the Stevens Honor System
# Problem 2
list2 = []
numbers = int(input("How many numbers will you enter?"))
print("Enter numbers")
for i in range(numbers):
    data = int(input())
    list2.append(data)
print(sum(list2))