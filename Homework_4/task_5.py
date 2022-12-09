#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

A = int (input('Введите А:'))
B = int (input('Введите В:'))
C = int (input('Введите C:'))
A1 = int (input('Введите А1:'))
B1 = int (input('Введите B1:'))
C1 = int (input('Введите C1:'))
k = 2
with open ("file1.txt", "w") as data1:
   data1.write(f'{A}*x^{k} + {B}*x + {C} = 0')
with open ("file2.txt", "w") as data2:
    data2.write(f'{A1}*x^{k} + {B1}*x + {C1} = 0')
with open ("file3.txt", "w") as data3:
    data3.write(f'{A1+A}*x^{k} + {B1+B}*x + {C1+C} = 0')