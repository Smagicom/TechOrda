#!/usr/bin/env python3
from correctdate import checkdate

def CheckSeason(d, m, y):
    y = int(y)
    m = int(m)
    d = int(d)
    if checkdate(d, m, y):
         match m:
               case 6 | 7 | 8:
                     print("Summer")

               case 9 | 10:
                     print("Fall")

               case 11 | 12 | 1 | 2:
                     print("Winter")
        
               case 3 | 4 | 5:
                     print("Spring")    
    else:
          print("Invalid date!")

d, m, y = input("Please enter date in format dd.mm.yyyy: ").split(".")
CheckSeason(d, m, y)