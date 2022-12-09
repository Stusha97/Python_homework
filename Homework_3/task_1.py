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