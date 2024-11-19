def sum_1_to_n(n):
    return n * (n + 1) // 2

def count_leap_years(n):
    def count(year):
        if year < 0:
            return 0
        return year // 4 - year // 100 + year // 400
    return count(n)

def swap_bits(a):
    return (a & 0b00001111) << 4 | (a & 0b11110000) >> 4

def sort_three_nums(a, b, c):
    return sorted([a, b, c])

def median(array):
    if not array:
        return None
    array.sort()
    mid = len(array) // 2
    return array[mid - 1] if len(array) % 2 == 0 else array[mid]

def miss_you(array1, array2):
    return sorted(set(array2) - set(array1))

def perfectly_balanced(array):
    total_sum = sum(array)
    left_sum = 0
    for i in range(len(array)):
        if left_sum == (total_sum - left_sum - array[i]):
            return True
        left_sum += array[i]
    return False

def stock_buy(m, s):
    indices = {}
    for i, price in enumerate(s):
        if m - price in indices:
            return sorted([i, indices[m - price]])
        indices[price] = i

def hanoi_tower(n, source=1, target=3, auxiliary=2):
    if n == 1:
        print(f"Диск 1 с башни {source} переложить в башню {target}")
    else:
        hanoi_tower(n - 1, source, auxiliary, target)
        print(f"Диск {n} с башни {source} переложить в башню {target}")
        hanoi_tower(n - 1, auxiliary, target, source)

print(sum_1_to_n(5))
print(count_leap_years(4))
print(swap_bits(15))
print(sort_three_nums(3, 2, 1))
print(median([1, 2, 3]))
print(miss_you([1, 1, 3, 2, 5], [1, 3, 9, 1, 5, 7]))
print(perfectly_balanced([1, 2, 9, 8, 5, 7]))
print(stock_buy(8, [8, 7, 3, 1, 3, 10]))
hanoi_tower(5)
