#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int (input('Введите x:'))
y = int (input('Введите y:'))
def chetvert (x,y):
    if x > 0 and y > 0:
        return ('1')
    elif x < 0 and y > 0:
        return ('2')
    elif x < 0 and y < 0:
        return ('3')
    elif x > 0 and y < 0:
        return (' 4')
    else:
        return ('0')
print (chetvert(x,y))