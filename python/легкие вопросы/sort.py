def sort(array):
    end=False
    while end==False:
        end=True
        for i in range(len(array)-1):           
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
                end=False
    print(array)

sort([4,34,6,3,1,45,2,0,-12,53,8,114,2])