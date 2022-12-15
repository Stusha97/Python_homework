# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0'''

import random
k = int(input('Введите натуральную степень = '))
list = [] 
for i in range(k+1):
    list.append(random.randint(0, 100))
polynomial = []
for i in range (len(list)):
    if list[i] != 0:
        if i == 0:
            polynomial.append(f'{list[i]}')
        elif i == 1:
            polynomial.append(f'{list[i]}*x')
        else:
            polynomial.append(f'{list[i]}*x^{i}')
with open ('file.txt', 'w') as data:
    data.write ('+'.join(polynomial[::-1]) + '= 0')