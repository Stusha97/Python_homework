#Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

num = int (input('Введите номер четверти:'))

def chetvert (num):
     if num == 1:
         return ('x = (0;+inf), y = (0;+inf)')
     elif num == 2:
         return ('x = (-inf;0), y = (0;+inf)')
     elif num == 3:
         return ('x = (-inf;0), y = (-inf;0)')
     elif num == 4:
         return ('x = (0;+inf), y = (-inf;0)')
     else:
         return ('неправильный номер четверти,введите 1 или 2 или 3 или 4')
print (chetvert(num))