#Условия 
##int-cmp
Дается два числа a и b. Вернуть:
1, если a > b
0, если a = b
-1, если a < b
Sample Input:
1 0
Sample Output:
1

ответ:
def int_cmp(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1
a, b = map(int, input().split())
print(int_cmp(a, b))        

##max-of-three
Дается три числа a, b и c. Вернуть максимальное число из них.
Sample Input:
42 1 0
Sample Output:
42

ответ
def max_of_three(a, b, c):
    return max(a, b, c)
a, b, c = map(int, input("Введите три числа через пробел: ").split())
print(max_of_three(a, b, c))

#Циклы
##sqr-sum-1-n
Вернуть сумму квадратов чисел от 1 до n включительно.
Ограничения
1 <= n <= 10860
Sample Input:
3
Sample Output:
14

ответ
def sqr_sum(n):
    return (n * (n + 1) * (2 * n + 1)) // 6
n = int(input("Введите число n: "))
print(sqr_sum(n))





##print-even-a-b
Вывести в консоль четные числа в диапазоне от a включительно до b включительно.
Sample Input:
0 4
Sample Output:
0 2 4
 ответ
 def print_even(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=" ")
a, b = map(int, input().split())
print_even(a, b)

##pow-a-b
Вернуть число a в степени b. Используя цикл.
Ограничения
b > 0
a^b входит в ограничения типа int
Sample Input:
2 6
Sample Output:
64
 ответ
 def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result
a, b = map(int, input().split())
print(power(a, b))


##calc-deposit
Написать функцию, которая возвращает сколько будет денег на депозите через n месяцев при ставке k и изначальном балансе b тенге.
Вознаграждения по депозиту начисляются каждый месяц.
Ограничения
0 <= n <= 10000
0 <= k <= 100
0 <= b <= 10000
Пример
Если положить на депозит 1000 тенге на срок в 1 месяц со ставкой в 5%, то через месяц на счете будет 1050 тенге.
Sample Input:
1 5 1000
Sample Output:
1050.0

ответ
def calc_deposit(n, k, b):
    for _ in range(n):
        b += b * (k / 100)
    return b
n, k, b = map(int, input().split())
print(calc_deposit(n, k, b))



#Массивы
##Min


Реализовать функцию min, которая возвращает минимальное число из массива. Если в массиве нет элементов, верните 0.
Ограничения
0 <= array.length <= 10_000
Sample Input:
[1, 2, 3]
Sample Output:
1
 ответ
 def min_array(arr):
    if len(arr) == 0:
        return 0
    return min(arr)
arr = [1, 2, 3]
print(min_array(arr))

##range
Реализовать функцию range, которая создает массив размером n, заполняет ячейки значениями от 1 до n и возвращает созданный массив.
Пример
int[] arr = range(5);

for (int i = 0; i < arr.length; i++) {   
    System.out.print(arr[i] + " ");
}
// Напечатает
// 1 2 3 4 5
Ограничения
0 < n <= 10_000
Sample Input:
5
Sample Output:
[1, 2, 3, 4, 5]

ответ
def range_array(n):
    return [i for i in range(1, n + 1)]
n = int(input())
print(range_array(n))

##sum
Реализовать функцию sum, которая возвращает сумму чисел массива.
Пример
int array[] = {7, 5, 9, 1, 4};
int sum_number = sum(array);

print(sum_number); // <-- выведет 26
Ограничения
0 <= array.length <= 10_000
Sample Input:
[1, 2, 3]
Sample Output:
6
 ответ
 def sum_array(arr):
    return sum(arr)
arr = [1, 2, 3]
print(sum_array(arr))

##sort
Реализовать функцию sort, которая принимает массив array(int[]). Функция должна отсортировать массив по возрастанию.
Подсказка: https://habr.com/ru/post/204600/
Запрещено использовать Arrays.sort.
Пример
int array[] = {7, 5, 9, 1, 4};
sort(array);

for (int i = 0; i < array.length; i++) {   
    System.out.print(array[i] + " ");
}
// Напечатает
// 1 4 5 7 9
Ограничения
0 <= array.length <= 10_000
Sample Input:
[3, 2, 1]
Sample Output:
[1, 2, 3]

ответ
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
arr = [7, 5, 9, 1, 4]
selection_sort(arr)
print(arr)
