#Реализуйте алгоритм перемешивания списка.
n = int(input ('Введите количество элементов n:'))
import random
list1 = []
for i in range (n):
    list1.append (random.randint (0, n+1))
print(f'Первоначальный список {list1}')

list2= list1 [:]

for x in range (n):
    index = random.randint(0,n-1)
    temp = list2[x]
    list2[x]= list2[index]
    list2[index]= temp
print(f'Перемешанный список {list2}')
