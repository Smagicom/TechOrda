n = int(input())

if 1 <= n <= 10860:
    sum = 0
    for i in range(1, n + 1):
        sum += i * i
    print(sum)
else: 
    print("Wrong number")