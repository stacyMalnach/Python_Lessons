# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

num = int(input("Input digital limit: "))
pi = math.pi
new_pi = (round(pi, num))
print(f"Pi is {new_pi} for digital number {num}.")

# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

num = int(input("Input number: "))
i = 2
lst = []
while i <= num:
    if num % i == 0:
        num = num // i
        i == 2
        lst.append(i)
    else:
        i += 1

print(f"Multipliers of {num} is: {lst}." )

# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

size = int(input("Input size of list: "))
my_lst = []

for i in range(size):
    x = int(input("Input numbers for list: "))
    my_lst.append(x)
print(f"Generated list is: {my_lst}.")

new_lst = []
for i in my_lst:
        if i not in new_lst:
            new_lst.append(i)
print(f"Uniq list: {new_lst}.")