'''
    Author:  Rowland DePree             Server_Tic_Tac_Toe.py

    This is a server file design to allow the user to play tic tac toe with one other player.  The server will always be
    player 2 the this game.  The standard rules for tic tac toe are used.
'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 12345

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


def check_win():
    if game_board[0][0] == game_board[0][1] == game_board[0][2]:
        return game_board[0][0]
    elif game_board[1][0] == game_board[1][1] == game_board[1][2]:
        return game_board[1][0]
    elif game_board[2][0] == game_board[2][1] == game_board[2][2]:
        return game_board[2][0]
    elif game_board[0][0] == game_board[1][0] == game_board[2][0]:
        return game_board[0][0]
    elif game_board[0][1] == game_board[1][1] == game_board[2][1]:
        return game_board[0][1]
    elif game_board[0][2] == game_board[1][2] == game_board[2][2]:
        return game_board[0][2]
    elif game_board[0][0] == game_board[1][1] == game_board[2][2]:
        return game_board[0][0]
    elif game_board[0][2] == game_board[1][1] == game_board[2][0]:
        return game_board[0][2]
    else:
        if (game_board[0][0] == 'X' or game_board[0][0] == 'O') and (
                        game_board[0][1] == 'X' or game_board[0][1] == 'O') and (
                        game_board[0][2] == 'X' or game_board[0][2] == 'O') and (
                        game_board[1][0] == 'X' or game_board[1][0] == 'O') and (
                        game_board[1][1] == 'X' or game_board[1][1] == 'O') and (
                        game_board[1][2] == 'X' or game_board[1][2] == 'O') and (
                        game_board[2][0] == 'X' or game_board[2][0] == 'O') and (
                        game_board[2][1] == 'X' or game_board[2][1] == 'O') and (
                        game_board[2][2] == 'X' or game_board[2][2] == 'O'):
            return -1
        else:
            return 'E'


def print_board():
    for row in range(3):
        print game_board[row]


def game_reset():
    for row in range(3):
        for col in range(3):
            game_board[row][col] = 'E'


def main():
    s.bind((host, port))
    s.listen(2)

    while True:
        game_over = False
        conn, addr = s.accept()
        print 'Got connection from' + str(addr)
        print '\nWelome to Tic Tac Toe Socket Edition!' \
              '\nStandard tic tac toe rules are use.  This means you must get' \
              '\nthree in a row to win.' \
              '\nmEmpty spaces on the board are represented by an E' \
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
            print 'Waiting on Player 1....\n'
            move = conn.recv(1024)
            update_board_X(int(move))
            winner = check_win()

            if winner == 'X':
                print 'Player 1 Wins!'
                conn.send('Player 1 Wins!')
                game_over = True
            elif winner == 'O':
                print 'Player 2 Wins!'
                conn.send('Player 2 Wins!')
                game_over = True
            elif winner == 'E':
                print_board()
                move = validate_move()
                update_board_O(move)
                conn.send(str(move))
            else:
                print 'Tie! No One Wins!'
                conn.send('Tie! No One Wins!')
                game_over = True
        conn.close()
        game_reset()


if __name__ == '__main__':
    main()
