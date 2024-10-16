def range(n):
    array1 = [0] * n
    i = 0
    while i < n:
        array1[i] = i+1
        i+=1
    return array1

number = int(input("Enter number: "))
array2 = range(number)

i = 1

while i < number-1:
    if number%array2[i]==0:
        print(number, " is not natural")
        break
    else:
        i+=1

if i == number-1:
    print(number, " is natural")