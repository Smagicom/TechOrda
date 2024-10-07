#!/usr/bin/env python3

a, b = input("Type two numbers: ").split()
a = int(a)
b = int(b)
if a > b:
    print("1")
elif a == b:
    print("0")
else:
    print("-1")

