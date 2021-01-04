#Problem 2 Philip Brendel
#I pledge my honor that I have followed the Stevens Honor code

def Sum(nums):
    Sum = 0
    for i in nums:
        Sum += i
    return Sum

def main():
    nums = [0,1,2,3,4,5,6,7,8,9]
    num = Sum(nums)
    print(num)

main()
