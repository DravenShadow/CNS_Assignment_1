import socket

game_board = 'test'

s = socket.socket()
host = socket.gethostname()
port = 12345
player_dict = {}


def send_game_board():
    counter = 0
    s.bind((host, port))
    s.listen(5)
    while counter < 3:
        c, addr = s.accept()
        counter += 1
        player = ('player_' + str(counter))
        player_dict[player] = addr
        c.send(str(game_board))
        print('Sent game board to ' + str(addr))
        c.close()
        print player_dict


def recive_move():
    player_move = ''
    s.bind((host, port))
    s.listen(5)
    while True:
        c, addr = s.accept()
        player_move = c.recv(1024)
        print 'Move recieved from ' + addr
        c.clse()


def make_move(row, col, player_number):
    pass


while True:
    send_game_board()
