#!/usr/bin/env python3

def sum_nums(nums):
    if 0 <= len(nums) <= 10000:
        sum = 0
        for i in nums:
            sum += i
        print(sum)
    else:
        print("The length of the list is out of the acceptable range!")
nums = input("Please enter the numbers: " )
numbers = list(map(int, nums.split()))
sum_nums(numbers)