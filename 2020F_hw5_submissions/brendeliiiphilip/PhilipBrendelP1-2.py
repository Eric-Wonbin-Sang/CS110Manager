#Problem 1 Philip Brendel
#I pledge my honor that I have followed the Stevens Honor code

def squared(nums):
    count = 0
    for i in nums:
        nums[count] = i**2
        count += 1
    return nums

def main():
    nums = [0,1,2,3,4,5,6,7,8,9]
    nums = squared(nums)
    print(nums)

main()
