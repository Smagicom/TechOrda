#!/usr/bin/env python3

def min_num(nums):
    if not nums:  
        return None
    res = nums[0]
    for i in nums:
         if i < res:
             res = i
    return res 
          
num_input = input("Please enter the numbers, there must be spaces between the numbers.: ")
numbers = list(map(int, num_input.split()))
print("The mininmum number is: ", min_num(numbers))

          