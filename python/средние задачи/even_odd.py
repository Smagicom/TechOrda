#!/usr/bin/env python3

def even_odd(n):
    if n % 2 == 0:
        print("Even!")
    else:
        print("Odd!")
try:
    num = int(input("Please enter a number: "))
    even_odd(num)
except ValueError:
    print("Invalid input! Please enter a valid number.")