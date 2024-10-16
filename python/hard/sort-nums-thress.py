def sortn(a, b, c):
    if a <= b and a <= c:
        if b <= c:
            print(a, " ", b, " ", c)
        else:
            print(a, " ", c, " ", b)
    elif b <= a and b <= c:
        if a <= c:
            print(b, " ", a, " ", c)
        else:
            print(b, " ", c, " ", a)
    else:
        if b <= a:
            print(c, " ", b, " ", a)
        else:
            print(c, " ", a, " ", b)

sortn(3, 2, 1)