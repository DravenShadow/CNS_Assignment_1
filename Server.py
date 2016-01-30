'''
    Author:  Rowland DePree             Server.py

    This is a server file design to allow for a remote connection form a different computer.  To do this, you will need
    to know your IP address and the port number you wish to use for outside communication.  Change the host name to the
    IP address and the port number to the port number you are using.  It will then wait for a client program to connect
    to it and send off the the date and time it connect to the client while print out in the console the address of the
    computer that it connected from.
'''

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
    c.close()
