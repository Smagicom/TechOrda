def calc(b, k, n):
    for i in range(n):
        b += b*k/100
    print(b)

calc(1000, 5, 1)