import math

number=int(input("Enter number: "))
bit = [0, 0, 0, 0, 0, 0, 0, 0]
res = 0

for i in range(len(bit)):
    if number >= 1:
        bit[i]=number%2
    number=int(number/2)

for i in range(len(bit)):
    res += bit[i] * pow(2, (7-i))

print(res)