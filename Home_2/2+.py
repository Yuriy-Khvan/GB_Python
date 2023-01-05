# 1. Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# a = float(input('Введите число '))
# len_num = len(str(a))-1

# while a != int(a):
#     a = round(a * 10, len_num)
#     print(a)
# print(a)

# sum = 0
# while a > 0:
#     sum +=a%10
#     a = a//10
# print(sum)

# 2.Напишите программу, которая принимает на вход число N и выдает
#  набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите число для вычисления факториала: '))
# fact_mult = []
# factorial = 1
# for i in range(2, n+2):
# 	fact_mult.append(factorial)
# 	factorial*=i
# print(fact_mult)

# 3. Задайте список из n чисел последовательности (1+1\n)^n и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# n = int(input('Введите число n для расчета последовательности '))
# dict_num = {}
# sum_n = 0
# for i in range(1,n+1):
#     sum_n += round((1+1/i)**i,2)
#     dict_num[i] = round((1+1/i)**i,2)
# print(dict_num)
# print(sum_n)

# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# n = int(input('Введите количество элементов n '))
# list_n = [i for i in range(-n,n+1)]
# print(list_n)

# file = open("File.txt","r")
# a = file.readlines()
# print(a)
# for i in range(len(a)):
# 	a[i] = int(a[i].strip())
# print(a)

# mult = 1
# for i in range(len(a)):
# 	mult *= list_n[a[i]]
# print(mult)

# 5. Реализуйте алгоритм перемешивания списка.

# import random
# a = [1,2,3,4,5,6,7,8,9]
# print(a)
# random.shuffle(a)
# print(a)