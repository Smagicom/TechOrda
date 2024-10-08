#!/usr/bin/env python3

def min_num(nums):
    if 0 <= len(nums) <= 10000:
        if not nums:  
            print("The list is empty!")
            return None
        res = nums[0]
        for i in nums:
           if i < res:
              res = i
        return res
    else:
        print("The numbers out of range!") 
          
num_input = input("Please enter the numbers, there must be spaces between the numbers.: ")
numbers = list(map(int, num_input.split()))
print("The mininmum number is: ", min_num(numbers))

          