
# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# Homework 3 task 3
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
list = input('Введите список:').split (' ')
print (list)
list2= []
for i in range (len(list)):
    list2.append (round(float(list[i])% 1,2))
print(list2)
max = list2[0]
min = list2[0]
i = 1
while i < len (list2):
    if list2 [i] > max:
         max = list2 [i]
    if list2 [i] < min:
        min = list2 [i]
    i = i+1
print(f'Разница между максимальной и минимальной дробной частью: {round(max-min,2)}')

#lambda,map

a = input('Введите список:').split (' ')
print (a)
f = lambda i :round(float(i)% 1,2)
list2= list(map(f,a))
print(list2)
print(max(list2)- min(list2))
