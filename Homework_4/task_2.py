#2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input ('Введите число:'))
list = []
for i in range(2, n//2+1):
        while n % i == 0:
            list.append(i)
            n = n//i
if n!=1:
    list.append(n)
print(list)