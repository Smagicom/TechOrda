#!/usr/bin/env python3

def listperfect(n):
    perfect_nums = [6, 28, 496]
    s = []
    try:
        n = int(n)
        if n < 0 or n > 1000:
            print("The number is out of range!")
            return []
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return []
    
    
    for i in range (1, n):
        if i in perfect_nums:
            s.append(i)
    return s
    
           
num = input("Please enter the number: ")
print(listperfect(num))
