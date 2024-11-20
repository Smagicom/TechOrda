#!/usr/bin/env python3
import math

def is_perfect_square(x):
    s = int(math.sqrt(x))
 
    return  s * s == x

def fibnum(n):
    
    pos_test = 5 * (n ** 2) + 4
    neg_test = 5 * (n ** 2) - 4
    
    return is_perfect_square(pos_test) or is_perfect_square(neg_test)


num = int(input("Enter a number: "))
if fibnum(num):
    print(f"{num} is a Fibonacci number")
else:
    print(f"{num} is not a Fibonacci number")