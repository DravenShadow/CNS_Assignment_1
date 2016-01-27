import socket

tic_tac_toe_board = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]

recieve_board_list = []

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))
r = s.recv(1024)
print('Receving Game Board...')
while r:
    recieve_board_list.append(r)
    r = s.recv(1024)
print('Game board has been received')
print(recieve_board_list)
s.close
