# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# from random import randint
# no_list = [randint(0,25) for i in range(randint(1,10))]
# print(no_list)
# sum_n = 0
# for i in range(1,len(no_list),2):
# 	sum_n+=no_list[i]
# print(sum_n)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# from random import randint
# no_list = [randint(0,25) for i in range(randint(5,10))]
# print(no_list)
# num_mult = []
# length = len(no_list)
# middle = length//2 + length%2
# for i in range(middle):
#     num_mult.append(no_list[i] * no_list[length - i - 1])
# print(num_mult)

# 3.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random
# def fract(num):
# 	return round(num%1,2)

# list_num = [round(random.uniform(0,20),2) for i in range(random.randint(5,10))]
# list_num.append(5.0)
# print(list_num)
# list_num_fract = []
# for i in list_num:
# 	if i%1!=0:
# 		list_num_fract.append(fract(i))
# print(list_num_fract)
# max_num,min_num = list_num_fract[0],list_num_fract.pop(0)
# for  i in list_num_fract:
# 	if i > max_num:
# 		max_num = i
# 	elif i < min_num:
# 		min_num = i
# print(max_num - min_num)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# def num_bin(num, res = ""):
# 	if num ==0:
# 		return res[::-1]
# 	res += str(num%2)
# 	return num_bin(num//2, res)

# n = int(input('Введите число для перевода в двоичное '))
# print(num_bin(n))


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#  [Негафибоначчи]
# def positive_fib(n):
# 	pos_list = [0,1]
# 	for i in range(n-1):
# 		pos_list.append(pos_list[-2] + pos_list[-1])
# 	return pos_list
# def negative_fib(n):
# 	negat_list = [1,0]
# 	for i in range(n-1):
# 		negat_list.insert(0,negat_list[1] - negat_list[0])
# 	return negat_list
# print(negative_fib(8) + positive_fib(8)[1:])  