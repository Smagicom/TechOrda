def median(array):
    i = int(len(array)/2)
    if len(array)%2==1:
        print(array[i])
    else:
        print(array[i-1])

median([1, 2, 3, 4])