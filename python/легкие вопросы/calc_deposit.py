#!/usr/bin/env python3

def calc_deposit(duration:int, rate:float, sum:int):
    res = sum
    for i in range(duration):
        res += res * rate / 100
    print(res)
duration, rate, sum = input("Type number the folowing order duration, rate, sum: ").split()

calc_deposit(int(duration), float(rate), int(sum))

