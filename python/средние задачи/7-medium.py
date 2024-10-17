def perfect(number:int):
    count=0
    i=1
    while i<number:
        if number%i==0:
           count+=i
           i+=1
        else:
            i+=1
    if number==count:
        print("nubmer",number,"is perfect")
    else:
        print("nubmer",number,"is NOT perfect")

perfect(1915) 