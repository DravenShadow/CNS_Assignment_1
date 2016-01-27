import datetime as dt
import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    c.send(str(dt.datetime.now()))
    c.close()  # Close the connection
