a = int(input("a = "))
b = int(input("b = "))
list1 = []
while a <= b:
    if a%2 == 0:
        list1.append(a)
    a+=1
print(list1)