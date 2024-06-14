import random
import os

class TicTacToe:
    def __init__(self):
        self.reset()

    def print_board(self):
        print('')
        print(' ' + self.board[0][0] + ' | ' + self.board[0][1] + ' | ' + self.board[0][2])
        print('-----------')
        print(' ' + self.board[1][0] + ' | ' + self.board[1][1] + ' | ' + self.board[1][2])
        print('-----------')
        print(' ' + self.board[2][0] + ' | ' + self.board[2][1] + ' | ' + self.board[2][2])

    def reset(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.done = ''

    def check_win_or_draw(self):
        dict_win = {}

        for i in ['X', 'O']:
            dict_win[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
            dict_win[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_win[i]

            dict_win[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_win[i]
            dict_win[i] = (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_win[i]

            dict_win[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[1][1] == self.board[0][2] == i) or dict_win[i]
         
        if dict_win["X"]:
            self.done = 'X'
            print('X venceu!')
            return
        elif dict_win['O']:
            self.done = 'O'
            print('O venceu!')
            return

        c = 0

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    c += 1

        if c == 0:
            self.done = 'd'
            print('Empate!')
            return

    def get_player_move(self):
        invalid_move = True

        while invalid_move:
            try:
                print('Digite a linha do seu próximo lance (0, 1, ou 2):')
                x = int(input())

                print('Digite a coluna do seu próximo lance (0, 1, ou 2):')
                y = int(input())

                if x < 0 or x > 2 or y < 0 or y > 2:
                    print('Coordenadas inválidas. As coordenadas devem estar entre 0 e 2.')
                elif self.board[x][y] != ' ':
                    print('Posição já preenchida. Escolha outra posição.')
                    continue
                else:
                    invalid_move = False
                
            except Exception as e:
                print(e)
                continue
            
        self.board[x][y] = 'X'

    def make_move(self):
        list_move = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    list_move.append((i, j))

        if len(list_move) > 0:
            x, y = random.choice(list_move)
            self.board[x][y] = 'O'

tic_tac_toe = TicTacToe()
tic_tac_toe.print_board()

next_game = 0

while next_game == 0:
    os.system('clear')

    tic_tac_toe.print_board()
    
    while tic_tac_toe.done == '':
        tic_tac_toe.get_player_move()
        tic_tac_toe.check_win_or_draw()
        if tic_tac_toe.done != '':
            break
        tic_tac_toe.make_move()
        tic_tac_toe.check_win_or_draw()
        if tic_tac_toe.done != '':
            break

        os.system('clear')

        tic_tac_toe.print_board()

    print('Digite 1 para sair do jogo ou qualquer tecla para jogar novamente.')

    next_game = input()

    if next_game == '1':
        break
    else:
        tic_tac_toe.reset()
        next_game = 0
