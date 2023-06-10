# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 
# 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

# Решение:

# n = int(input('Введите количество элементов первого массива: '))
# m = int(input('Введите количество элементов второго массива: '))
# a = []
# for i in range(n):
#     a += list(map(int, input().split()))
# print(a)
# b = []
# for i in range(m):
#     b += list(map(int, input().split()))
# print(b)
# result = []
# for i in range(0, n-1):
#     if a[i] not in b:
#         result.append(a[i])
# print(result)

# a = {'3', '1', '3', '4', '2', '4', '12'}
# b = {'4', '15', '43', '1', '15', '1'}
# print(sorted(a.difference(b)))
# print(a-b)
# a = (int, input('Введите элементы первого массива: ').split())
# b = (int, input('Введите элементы второго массива: ').split())
# print(a.difference(b))

# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)

# Решение:
# n = int(input('Введите количество элементов первого массива: '))
# a = []
# for i in range(n):
#     a += list(map(int, input().split()))
# print(a)
# count = 0
# for i in range(1, n-1):
#     if a[i] > a[i-1] and a[i] > a[i+1]:
#         count = count + 1
# print(count)

# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# Решение:

# a = int(input('Введите число: '))
# d = int(input('Введите шаг: '))
# n = int(input('Введите количество элементов: '))
# result = [a + (i-1) * d for i in range(1, n+1)]
# print(result)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

# Решение:

# mass = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min = int(input('Введите минимальное число: '))
# max = int(input('Введите максимальное число: '))
# for i in range(len(mass)):
#     if min <= mass[i] <= max:
#         print(i)