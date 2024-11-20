a=float(input("vvedite a: "))
b=float(input("vvedite b: "))
c=float(input("vvedite c: "))
if a>=b and a>=c:
    print("max number is: ",a)
elif b>=c and b>a:
    print("max number is: ",b)
else:
    print("max number is: ",c)