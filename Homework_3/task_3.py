# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
list = input('Введите список вещественных чисел:').split (' ')
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