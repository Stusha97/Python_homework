# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

player1 = input ('Игрок 1, введите имя:')
player2 = input ('Игрок 2, введите имя:')
from random import randint

def lottery ():
    first = range(randint(1,2))
    if first == 1:
            first = player1
            print('Первым ходит игрок 1')
    else:
            first = player2
            print('Первым ходит игрок 2')
    return first

first = lottery()
candies = 100
while candies > 0:
    if first == player1:
        move_p1 = int(input(f'{player1} введите число от 1 до 28: '))
        if move_p1 > 0 and move_p1 <= 28 and (candies-move_p1) > 0: 
            candies = candies - move_p1
            print(f'Осталось конфет: {candies}')
        elif candies - move_p1 == 0:
            print( f'Победил игрок {player1}')
            break
        move_p2 = int (input(f'{player2} введите число от 1 до 28: '))
        if move_p2 > 0 and move_p2 <= 28 and (candies-move_p2) > 0:
            candies= candies - move_p2
            print(f'Осталось конфет: {candies}')
        elif candies-move_p2 == 0:
            print(f'Победил игрок {player2}')
            break
    else:
        move_p2 = int (input(f'{player2} введите число от 1 до 28:  '))
        if move_p2 > 0 and move_p2 <= 28 and (candies-move_p2) > 0:
            candies= candies- move_p2
            print(f'Осталось конфет: {candies}')
        elif candies-move_p2 == 0:
            print(f'Победил игрок {player2}')
            break
        move_p1 = int(input(f'{player1} введите число от 1 до 28:  '))
        if move_p1 > 0 and move_p1 <= 28 and (candies-move_p1) > 0: 
            candies = candies- move_p1
            print(f'Осталось конфет: {candies}')
        elif candies - move_p1 == 0:
            print( f'Победил игрок {player1}')
