ary = [1, 2, 9, 8, 5, 7]
res=bool

for i in range(len(ary)-2):
    sum1=0
    sum2=0
    for j in range(i+1):
        sum1+=ary[j]
    for k in range(len(ary)-2-i):
        sum2+=ary[k+i+2]
    if sum1 == sum2:
        res=True

if res==True:
    print("true")
else:
    print("false")
