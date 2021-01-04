#Kayla Batzer
#HW 5 P1
#I pledge my honor to abide by the Stevens honor code

def square(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]

def main():
    inputList = [1, 2, 3, 4, 5]
    square(inputList)
    print(inputList)
main()
