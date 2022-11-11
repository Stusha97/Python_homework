#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
#Позиции хранятся в файле file.txt в одной строке одно число.
n= int(input('Введите число элементов:'))
import random
list = [random.randint(-n,n)for i in range (n)]
print(list)
with open ('file.txt', 'w') as data:
    for i in range (0,n):
        data.write (str(i)+ '\n')

pos_1 = int(input(f'Укажите 1 позицию (от 0 до {n-1}):'))
pos_2 = int(input(f'Укажите 2 позицию (от 0 до {n-1}):'))
if 0<=pos_1<=(n-1) and 0<=pos_2<=(n-1):
    path = 'file.txt'
    data = open(path, 'r')   
    for line in data:
        result = list[int(pos_1)]*list[int(pos_2)]
        print (f'Элемент на позиции {line}={list[int(line)]}')
    data.close()
    print(f'Произведение элементов на  указанных позициях = {result} ')
else:
    print (f'Таких позиций нет, введите от 0 до {n-1}')