import socket

s = socket.socket()
host = ''
port = 54321

game_board = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]


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
        return 0


def main():
    game_over = False

    while not game_over:
        print(game_board)
        move = raw_input('Enter in move: ')
        update_board_X(move)
        s.sendto(move, (host, port))
        data = s.recv(1024)
        update_board_O(data)
        winner = check_win()

        if winner == 'X':
            print 'Player 1 Wins!'
            print game_board
            game_over = True
        elif winner == 'O':
            print 'PLayer 2 Wins!'
            print game_board
            game_over = True


if __name__ == '__main__':
    main()
