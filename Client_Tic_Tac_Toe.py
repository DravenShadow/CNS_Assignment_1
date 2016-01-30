'''
    Author:  Rowland DePree             Client_Tic_Tac_Toe.py

    This is a client file design to allow you to play tic tac toe with one other person who has the server file.  This
    file will always make this user player 1.  Standard tic tac toe rules apply.
'''
import socket

game_board = [['E', 'E', 'E'],
              ['E', 'E', 'E'],
              ['E', 'E', 'E']]


def update_board_X(move):
    if move == 1:
        game_board[0][0] = 'X'
    elif move == 2:
        game_board[0][1] = 'X'
    elif move == 3:
        game_board[0][2] = 'X'
    elif move == 4:
        game_board[1][0] = 'X'
    elif move == 5:
        game_board[1][1] = 'X'
    elif move == 6:
        game_board[1][2] = 'X'
    elif move == 7:
        game_board[2][0] = 'X'
    elif move == 8:
        game_board[2][1] = 'X'
    elif move == 9:
        game_board[2][2] = 'X'


def update_board_O(move):
    if move == 1:
        game_board[0][0] = 'O'
    elif move == 2:
        game_board[0][1] = 'O'
    elif move == 3:
        game_board[0][2] = 'O'
    elif move == 4:
        game_board[1][0] = 'O'
    elif move == 5:
        game_board[1][1] = 'O'
    elif move == 6:
        game_board[1][2] = 'O'
    elif move == 7:
        game_board[2][0] = 'O'
    elif move == 8:
        game_board[2][1] = 'O'
    elif move == 9:
        game_board[2][2] = 'O'


def validate_move():
    move = input('Enter in your move: ')
    if move == 1 and game_board[0][0] == 'E':
        return move
    elif move == 2 and game_board[0][1] == 'E':
        return move
    elif move == 3 and game_board[0][2] == 'E':
        return move
    elif move == 4 and game_board[1][0] == 'E':
        return move
    elif move == 5 and game_board[1][1] == 'E':
        return move
    elif move == 6 and game_board[1][2] == 'E':
        return move
    elif move == 7 and game_board[2][0] == 'E':
        return move
    elif move == 8 and game_board[2][1] == 'E':
        return move
    elif move == 9 and game_board[2][2] == 'E':
        return move
    else:
        valid = False
        while not valid:
            new_move = input('INVALID MOVE! Please enter in a valid move: ')
            if new_move == 1 and game_board[0][0] == 'E':
                valid = True
                return new_move
            elif new_move == 2 and game_board[0][1] == 'E':
                valid = True
                return new_move
            elif new_move == 3 and game_board[0][2] == 'E':
                valid = True
                return new_move
            elif new_move == 4 and game_board[1][0] == 'E':
                valid = True
                return new_move
            elif new_move == 5 and game_board[1][1] == 'E':
                valid = True
                return new_move
            elif new_move == 6 and game_board[1][2] == 'E':
                valid = True
                return new_move
            elif new_move == 7 and game_board[2][0] == 'E':
                valid = True
                return new_move
            elif new_move == 8 and game_board[2][1] == 'E':
                valid = True
                return new_move
            elif new_move == 9 and game_board[2][2] == 'E':
                valid = True
                return new_move


def print_board():
    for row in range(3):
        print game_board[row]


def main():
    s = socket.socket()
    host = '192.168.1.7'
    port = 12345

    game_over = False

    s.connect((host, port))
    print '\nWelome to Tic Tac Toe Socket Edition!' \
          '\nStandard tic tac toe rules are use.  This means you must get' \
          '\nthree in a row to win.' \
          '\nBlank spaces are represented by E' \
          '\nEach space in board corresponds to a number.  When prompted to enter' \
          '\na move, enter the location you wish to move to.' \
          '\nBelow is the cheat sheet for where you can move.' \
          '\n1 | 2 | 3' \
          '\n_________' \
          '\n4 | 5 | 6' \
          '\n_________' \
          '\n7 | 8 | 9\n'
    print_board()
    while not game_over:
        move = validate_move()
        update_board_X(move)
        s.send(str(move))
        print 'Waiting for Player 2.... \n'

        data = s.recv(2014)
        if data == 'Player 1 Wins!':
            print data
            game_over = True
        elif data == 'Player 2 Wins!':
            print data
            game_over = True
        elif data == 'Tie! No One Wins!':
            print data
            game_over = True
        else:
            update_board_O(int(data))
            print_board()
    s.close()


if __name__ == '__main__':
    main()
