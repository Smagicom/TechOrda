i = 2
while i <= 1000:
    dls = list()
    j = 1
    for j in range(i):
        if i%(j+1)==0:
            dls.append(j+1)
    if sum(dls)/2 == i:
        print(i, " ")
    i+=1
