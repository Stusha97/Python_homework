# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# Homework 3 task 2

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
n = int(input ('Введите количество элементов n:'))
import random
import math
list = [random.randint(0,10) for i in range (n)]
print (list)
for i in range (int(math.ceil(len(list)/2))):
    p = list [i]*list[n-1-i]
    print(p, end = ' ')

#zip, list comprehension

n = int(input ('Введите количество элементов n:'))
import random
list1 = [random.randint(0,10) for i in range (n)]
print (list1)
zipped = list(zip(list1[:n//2+1:],list1[:n//2-1:-1]))
print(zipped)
p= [i*j for i,j in zipped]
print(p)
