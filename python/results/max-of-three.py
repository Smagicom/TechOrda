a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a > b and c < a:
    print(a)
elif b > a and c < b:
    print(b)
else: 
    print(c)