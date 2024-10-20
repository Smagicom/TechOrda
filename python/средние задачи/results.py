def check_even_odd():
    number = int(input("Введите число: "))
    if number % 2 == 0:
        print(f"{number} является четным.")
    else:
        print(f"{number} является нечетным.")

def check_palindrome():
    string = input("Введите строку: ")
    if string == string[::-1]:
        print(f"{string} является палиндромом.")
    else:
        print(f"{string} не является палиндромом.")

def is_prime():
    number = int(input("Введите число: "))
    if number <= 1:
        print(f"{number} не является простым числом.")
        return
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print(f"{number} не является простым числом.")
            return
    print(f"{number} является простым числом.")

def check_date():
    from datetime import datetime
    date_str = input("Введите дату (дд.мм.гггг): ")
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        print(f"{date_str} является корректной датой.")
    except ValueError:
        print(f"{date_str} не является корректной датой.")

def perfect_numbers():
    perfects = []
    for num in range(1, 1001):
        divisors_sum = sum(i for i in range(1, num) if num % i == 0)
        if divisors_sum == num:
            perfects.append(num)
    print(f"Совершенные числа в диапазоне от 0 до 1000: {perfects}")

def is_fibonacci():
    number = 25
    a, b = 0, 1
    while a < number:
        a, b = b, a + b
    if a == number:
        print(f"{number} является числом Фибоначчи.")
    else:
        print(f"{number} не является числом Фибоначчи.")

def check_perfect():
    number = int(input("Введите число: "))
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    if divisors_sum == number:
        print(f"{number} является совершенным числом.")
    else:
        print(f"{number} не является совершенным числом.")

def determine_season():
    date_str = input("Введите дату (дд.мм): ")
    day, month = map(int, date_str.split('.'))
    if (month == 12 and day >= 21) or (month <= 2) or (month == 3 and day < 21):
        season = "Зима"
    elif (month == 3 and day >= 21) or (month <= 5) or (month == 6 and day < 21):
        season = "Весна"
    elif (month == 6 and day >= 21) or (month <= 8) or (month == 9 and day < 21):
        season = "Лето"
    else:
        season = "Осень"
    print(f"Дата {date_str} попадает в {season}.")

check_even_odd()
check_palindrome()
is_prime()
check_date()
perfect_numbers()
is_fibonacci()
check_perfect()
determine_season()
