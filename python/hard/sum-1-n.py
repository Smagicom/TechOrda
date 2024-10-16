def sumn(n):
    if n < 1:
        return 0
    return n + sumn(n-1)

number = int(input("Enter number: "))
print(sumn(number))