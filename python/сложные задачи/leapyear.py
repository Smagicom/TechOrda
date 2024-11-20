#!/usr/bin/env python3
def leapYear(n):
    n = int(n)
    res = 0
    for i in range(1, n+1):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            res += 1
    return res
num = input("Please enter the number: ")
print(leapYear(num))