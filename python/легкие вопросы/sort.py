#!/usr/bin/env python3

def nums_sort(nums):
    if 0 <= len(nums) <= 10000:
        for i in range(len(nums) - 1): 
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
num_input = input("Please enter the numbers, there must be spaces between the numbers.: ")
numbers = list(map(int, num_input.split()))
print(nums_sort(numbers))
