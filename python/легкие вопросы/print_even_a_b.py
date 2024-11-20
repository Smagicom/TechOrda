#!/usr/bin/env python3

def even_num(a, b):
    num = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            num.append(i)
    print(num)
a, b = input("Type two numbers: ").split()
a = int(a)
b = int(b)
even_num(a, b)