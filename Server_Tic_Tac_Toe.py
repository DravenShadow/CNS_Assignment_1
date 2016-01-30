import socket
from _socket import SOL_SOCKET, SO_REUSEADDR

s = socket.socket()
host = socket.gethostname()
port = 12345
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 2)
s.bind((host, port))

game_over = False
tic_tac_toe_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

s.listen(5)

while not game_over:
    c, addr = s.accept()
    c.send(str(tic_tac_toe_board))
    c.close()

    print c.recv(1024)
    c.close()
