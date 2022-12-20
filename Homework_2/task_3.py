#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

def f(n): 
    list = []
    for i in range(1, n+1):
        list.append (round((1+1/i)**i,3))
    return list

n = int(input('Введите число элементов N: '))
print(f(n))

list= f(n) 
def sum_list (list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum
print(f'Сумма элементов= {sum_list(list)}')