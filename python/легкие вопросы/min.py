def min_num(array):
    if not array:
        return 0
    min=array[0]
    for i in range(len(array)):
        if min>array[i]:
            min=array[i]
    print("min number is",min)

min_num([1,2,3])


