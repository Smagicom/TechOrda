from datetime import datetime

# Задача 1: Проверка на четность
def check_even_odd():
    num = int(input("Введите число: "))
    if num % 2 == 0:
        print("Число четное")
    else:
        print("Число нечетное")

# Задача 2: Проверка на палиндром
def check_palindrome():
    s = input("Введите строку: ").lower()
    if s == s[::-1]:
        print("Строка является палиндромом")
    else:
        print("Строка не является палиндромом")

# Задача 3: Проверка на простое число
def is_prime():
    num = int(input("Введите число: "))
    if num < 2:
        print("Число не является простым")
        return
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Число не является простым")
            return
    print("Число является простым")

# Задача 4: Проверка корректности даты
def is_valid_date():
    date_str = input("Введите дату в формате ДД.ММ.ГГГГ: ")
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        print("Дата корректна")
    except ValueError:
        print("Дата некорректна")

# Задача 5: Поиск совершенных чисел в диапазоне
def perfect_numbers_in_range():
    def is_perfect(n):
        return sum(i for i in range(1, n) if n % i == 0) == n

    perfect_numbers = [i for i in range(1, 1001) if is_perfect(i)]
    print("Совершенные числа в диапазоне от 0 до 1000:", perfect_numbers)

# Задача 6: Проверка числа Фибоначчи
def is_fibonacci():
    num = int(input("Введите число: "))
    def is_perfect_square(x):
        return int(x ** 0.5) ** 2 == x

    if is_perfect_square(5 * num ** 2 + 4) or is_perfect_square(5 * num ** 2 - 4):
        print(f"Число {num} является числом Фибоначчи")
    else:
        print(f"Число {num} не является числом Фибоначчи")

# Задача 7: Проверка на совершенное число
def check_perfect_number():
    num = int(input("Введите число: "))
    if sum(i for i in range(1, num) if num % i == 0) == num:
        print(f"Число {num} является совершенным")
    else:
        print(f"Число {num} не является совершенным")

# Задача 8: Определение сезона по дате
def determine_season():
    date_str = input("Введите дату в формате ДД.ММ: ")
    day, month = map(int, date_str.split('.'))
    if (month == 12 and day >= 21) or month in [1, 2] or (month == 3 and day < 21):
        print("Это зима")
    elif (month == 3 and day >= 21) or month in [4, 5] or (month == 6 and day < 21):
        print("Это весна")
    elif (month == 6 and day >= 21) or month in [7, 8] or (month == 9 and day < 21):
        print("Это лето")
    else:
        print("Это осень")

# Тестирование всех функций
if __name__ == "__main__":
    check_even_odd()            # Задача 1
    check_palindrome()          # Задача 2
    is_prime()                  # Задача 3
    is_valid_date()             # Задача 4
    perfect_numbers_in_range()  # Задача 5
    is_fibonacci()              # Задача 6
    check_perfect_number()      # Задача 7
    determine_season()          # Задача 8
