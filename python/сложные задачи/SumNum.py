#!/usr/bin/env python3

def sum_of_range(a, z):
     a = int(a)
     z = int(z)
     n = z - a + 1
     return (n * (a + z)) // 2

a, z = input("Please enter the numbers: ").split()
print(sum_of_range(a, z))