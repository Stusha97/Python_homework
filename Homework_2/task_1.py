#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = float (input ('Введите вещественное число: '))
numbers = str (number)
sum = 0
for i in numbers:
    if i != ".":
        sum += int (i)
print (f'Сумма цифр числа = {sum}')