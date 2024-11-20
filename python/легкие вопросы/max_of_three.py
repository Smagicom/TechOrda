#!/usr/bin/env python3

def MaxNum(a):
    max_num = a[0]
    for i in a:
        if i > max_num:
            max_num = i
    return max_num
a = input("Please enter the 3 numbers: ")
a = list(map(int, a.split()))
print("The largest number is: ",  MaxNum(a))

