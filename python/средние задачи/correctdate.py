#!/usr/bin/env python3
def leapYear(y):
    y = int(y)

    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    
def checkdate(d, m, y):
    MAX_VALID_YR = 9999; 
    MIN_VALID_YR = 1800; 
    y = int(y)
    m = int(m)
    d = int(d)
    if y < int(MIN_VALID_YR) or y > int(MAX_VALID_YR):
        return False
    if m < 1 or m > 12:
        return False
    if  d < 1 or d > 31:
        return False
    
    if m == 2:
        if leapYear(y):
            return d <= 29
        else:
            return d <= 28
    if m == 4 or m == 6 or m == 9 or m == 11:
        return d <= 30
    return True
# d, m, y = input("Please enter date in format dd.mm.yyyy: ").split(".")
# print(checkdate(d, m, y))
# Please Uncomment if you want to check this function!
    