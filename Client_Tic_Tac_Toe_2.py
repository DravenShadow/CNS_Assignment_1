import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

while True:
    c, addr = s.accept()
    print(c.recv(1024))
    c.close()
