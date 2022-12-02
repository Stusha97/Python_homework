# Создайте программу для игры в ""Крестики-нолики"".
player1 = input ('Игрок 1, введите имя:')
player2 = input ('Игрок 2, введите имя:')

from random import randint
matrix = [1, 2, 3,4,5,6,7,8,9]
def print_matrix ():
    print(matrix [0],matrix [1],matrix [2])
    print(matrix [3],matrix [4],matrix [5])
    print(matrix [6],matrix [7],matrix [8])

matrix2 = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
for i in range (randint(1,2)):
    if i == 1:
        symbol1='X'
        symbol2='O'
    else:
        symbol1='O'
        symbol2='X'
def moves (move, symbol):
    index = matrix.index(move)
    if symbol == symbol1:
        matrix[index]=symbol1
    else:
        matrix[index]=symbol2
def game ():
    winner = ""
    for i in matrix2:
        if matrix [i[0]] == symbol1 and matrix [i[1]] == symbol1 and matrix [i[2]] == symbol1 :
            winner = player1
        elif matrix [i[0]] == symbol2 and matrix [i[1]] == symbol2 and matrix [i[2]] == symbol2 :
            winner = player2   
    return winner

game_over = False
while game_over != True:
    print_matrix()
    if  player1:
        symbol = symbol1
        move = int (input(f'{player1}, Ваш ход: '))
    moves(move,symbol)
    if  player2:
        symbol = symbol2
        move = int (input(f'{player2}, Ваш ход: '))
    moves(move,symbol)
    winner = game ()
    if winner != "":
        game_over=True
    else:
        game_over = False
print_matrix ()
print(f'Победитель: {winner}')