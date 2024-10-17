def perfect(number1:int,number2:int):
    i=number1
    while i<number2:
        count=0
        j=1
        while j<i:
            if i%j==0:
                count+=j
                j+=1
            else:
                j+=1
        if i==count and i!=0:
            print("nubmer",i,"is perfect")
        i+=1

perfect(0,1000) 