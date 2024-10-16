number = int(input("Enter number: "))
dls = list()
for i in range(number):
    if number%(i+1)==0:
        dls.append(i+1)
if sum(dls)/2 == number:
    print("The number is perfect")
else:
    print("The number is not perfect")