#!/usr/bin/env python3

def sum_sqr(n):
     num = 0
     if int(n) >= 1 and int(n) <= 10860:
        for i in range(1, n + 1):
              num += i ** 2
        print(num)
     else:
         print("Please provide a positive number and in a range of  1 to 10860!")
num = input("Please enter a number: ") 
num = int(num)
sum_sqr(num)