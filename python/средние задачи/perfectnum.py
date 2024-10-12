#!/usr/bin/env python3

def perfectnum(n):
    n = int(n)
    sum = 0
    if n <= 0 or n > 1000:
        return "The number out of range!"
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return "Perfect number"
    else:
        return "Not a perfect number"
    
num = input("Please enter the number: ")
print(perfectnum(num))