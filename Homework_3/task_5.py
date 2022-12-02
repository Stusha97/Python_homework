#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
n = int(input ('Введите число:'))
def fib (n):
    if n == 0:
         return 0
    if n in [1,2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def negfib (n):
    if n == 1:
        return 1
    if n == 2:
        return -1
    else:
        return negfib(n-2)-negfib(n-1)
list1 = []
list2 = []
for i in range (0,n+1):
    list1.append (fib(i))
for i in range (1,n+1):
    list2.append (negfib(i))
print(f'Cписок чисел Фибоначчи, в том числе для отрицательных индексов :{list2[::-1]+list1}')