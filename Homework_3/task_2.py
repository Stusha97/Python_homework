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