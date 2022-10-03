# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst = [2, 3, 5, 9, 3]
print(lst)
sum = 0
for i in range(len(lst)):
    if i%2 == 1:
        sum += lst[i]
print('Elemet_s sum of odd indexes: ', sum)



# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
lst_1 = []
for i in range(random.randint(1,10)):
    add_element = random.randint(5, 30)
    lst_1.append(add_element)
print(lst_1)

lst_2 = []
for i in range(len(lst_1) // 2):
    lst_2.append(lst_1[i] * lst_1[len(lst_1) - 1 - i])
print(lst_2)



# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Input number: '))
x = ''
while (num > 0):
    x = str(num % 2) + x
    num = num//2
print('Binary number of is:', x)




