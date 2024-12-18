#!/usr/bin/env python3

def list_range(n):
    size = int(n)
    if 0 <= size <= 10000:
        num = []
        for i in range(1, size + 1):
            num.append(i)
        print(num)
    else:
        print("The number is out of range!")

n = input("Please enter the size of list: ")
list_range(n)