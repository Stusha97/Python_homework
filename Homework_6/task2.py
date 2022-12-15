# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# Homework 3 task 1

#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

n = int(input ('Введите количество элементов n:'))
import random
list = [random.randint(0,10) for i in range (n)]
print (list)
sum=0
for i in range(len(list)):
    if i%2 != 0:
        sum+=list[i]
print(f'Сумма элементов на нечетных позициях: {sum}')

#list comprehension,enumerate

n = int(input ('Введите количество элементов n:'))
from random import randint
list = [randint(0,10) for i in range (n)]
print (list)
res = sum([list[i] for i,val in enumerate(list) if i%2 != 0])
print(res)


# или

#filter, lambda

n = int(input ('Введите количество элементов n:'))
from random import randint
data = [randint(0,10) for i in range (n)]
print (data)
res = sum(list(filter(lambda i:data.index(i)%2 != 0,data)))
print(res)