#!/usr/bin/env python3
import math
def prime_num(n):
    if n <= 1:
        return "The number isn't prime"
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return "The number isn't prime"
        
    return "The number is prime"

num = int(input("Please enter a number: "))
print(prime_num(num))