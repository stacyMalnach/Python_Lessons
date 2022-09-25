
#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

n = int(input('Input number from 1 to 7: '))

if n < 6:
	print('This day is NOT weekend =(')
	
if n > 5:
	print('This day is weekend =) Hheeee!')

#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Эта задача не совсем правильно решена, в коспекте урок 2 есть верное решение!!!

x = int(input('Input X: '))
y = int(input('Input Y: '))
z = int(input('Input Z: '))

left = not (x or y or z)
right = not x and not y and not z

if left == right:
	print('Statement is true.')

if left != right:
	print('Statement is false.')

#Напишите программу, которая принимает на вход координаты точки (X и Y), 
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
#(или на какой оси она находится).

x = int(input('Input x: '))
y = int(input('Input y: '))

if (x > 0 and y > 0):
	print ('Quarte of this coordinates is I')

if (x < 0 and y > 0):
	print ('Quarte of this coordinates is II')
	
if (x < 0 and y < 0):
	print ('Quarte of this coordinates is III')
	
if (x > 0 and y < 0):
	print ('Quarte of this coordinates is IV')

#Напишите программу, которая по заданному номеру четверти, показывает диапазон 
#возможных координат точек в этой четверти (x и y).

n = int(input('Input quarte: '))

if n == 1:
	print('X is positive, Y is positive')
	
if n == 2:
	print('X is negative, Y is positive')

if n == 3:
	print('X is negative, Y is negative')
	
if n == 4:
	print('X is positive, Y is negative')
		
#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x1 = float(input('Input first X coordinates: '))
y1 = float(input('Input first Y coordinates: '))
x2 = float(input('Input second X coordinates: '))
y2 = float(input('Input second Y coordinates: '))

xLine = x2 - x1
yLine = y2 - y1
distanse = xLine * xLine + yLine * yLine
import math
distanceQuarde = math.sqrt(distanse)
print(distanceQuarde)