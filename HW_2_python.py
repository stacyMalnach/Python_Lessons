# 1. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('Input number: '))
# d = {}

# for i in range(1, n + 1):
# 	d[i] = 3 * i + 1 
# print(d)



# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Input number: '))
# step = 1
# for i in range(1, n + 1):
#     step = step * i
#     print(step, end = ' ')



# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# - Для n = 5: сумма = 11,55

# n = int(input('Input number: '))
# lst = []
# for i in range (1, n + 1):
#     x = (1 + (1 / i))**i
#     lst.append(x)
# print(lst)

# sum = 0
# for i in lst:
#  	sum = sum + i
# print ('Sum of list_s elements is: ', sum)


