# Условие 1: int-cmp
def int_cmp(a: int, b: int) -> int:
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

# Условие 2: max-of-three
def max_of_three(a: int, b: int, c: int) -> int:
    return max(a, b, c)

# Условие 3: sqr-sum-1-n
def sqr_sum_1_n(n: int) -> int:
    return sum(i ** 2 for i in range(1, n + 1))

# Условие 4: print-even-a-b
def print_even_a_b(a: int, b: int) -> None:
    print(" ".join(str(i) for i in range(a, b + 1) if i % 2 == 0))

# Условие 5: pow-a-b
def pow_a_b(a: int, b: int) -> int:
    result = 1
    for _ in range(b):
        result *= a
    return result

# Условие 6: calc-deposit
def calc_deposit(n: int, k: float, b: float) -> float:
    return b * (1 + k / 100) ** n

# Массивы
# Условие 7: min
def min_in_array(arr: list) -> int:
    return min(arr) if arr else 0

# Условие 8: range
def range_array(n: int) -> list:
    return list(range(1, n + 1))

# Условие 9: sum
def sum_array(arr: list) -> int:
    return sum(arr)

# Условие 10: sort
def sort_array(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Тестовые примеры
if __name__ == "__main__":
    print(int_cmp(1, 0))  # Output: 1
    print(max_of_three(42, 1, 0))  # Output: 42
    print(sqr_sum_1_n(3))  # Output: 14
    print_even_a_b(0, 4)  # Output: 0 2 4
    print(pow_a_b(2, 6))  # Output: 64
    print(calc_deposit(1, 5, 1000))  # Output: 1050.0
    print(min_in_array([1, 2, 3]))  # Output: 1
    print(range_array(5))  # Output: [1, 2, 3, 4, 5]
    print(sum_array([1, 2, 3]))  # Output: 6
    print(sort_array([3, 2, 1]))  # Output: [1, 2, 3]

#  ТУТ были легкие воппросы


