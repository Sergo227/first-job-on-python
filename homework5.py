# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# Решение:

# A = int(input("введите число: "))
# B = int(input("введите степень: "))

# def degree(A, B):
#     if B == 0:
#         return 1
#     return A * degree(A, B-1)
# print (degree(A, B))

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

# Решение:

# a = int(input("введите первое число: "))
# b = int(input("введите второе число: "))
# c = b+1
# def sum(a, c):
#     if c == 0:
#         return 0
#     return a + sum(1, c-1)
# print(sum(a, c))