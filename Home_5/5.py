# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# line = 'фывабвйцу кенабвджэ, ячсабвнгш, йцукенгвба'
# while ',' in line or '.' in line or ';' in line or ',' in line:
#     line = line.replace(',', '')
# print(line)

# arr = line.split()
# print(arr)

# arr2 = []
# for word in arr:
#     if 'абв' not in word:
#         arr2.append(word)
# print(arr2)


import random

name1 = input("Введите имя первого игрока - ")
name2 = input("Введите имя второго игрока - ")
sweets = int(input("Введите желаемое количество конфет - "))
max_sweets = int(input("Введите максимум конфет за ход "))

first_turn = random.choice([name1,name2])

flag = name1 if first_turn == name1 else name2

while sweets>0:
	print(f"Ваш ход {flag}")

	turn = int(input("Введите желаемое количество конфет для взятия - "))

	while not 0<turn<max_sweets:
		print("Введите конфеты в диапазоне от 0 до ", max_sweets)
		turn = int(input("Введите желаемое количество конфет для взятия - "))
sweets -= turn
if sweets>0:
	print(f'конфет осталось - {sweets}')
else:
	print(f'конфет осталось - 0')

	flag = name2 if flag == name1 else name1
winner = name2 if flag == name1 else name1
print(f"Поздравляем, победил игрок {winner}")