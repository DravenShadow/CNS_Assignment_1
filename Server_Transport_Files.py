'''
    Author:  Rowland DePree             Server_Transport_Files.py

    This is a server file design to send a file from the server to the client file.  To do this you will need to know the
    path of the file location, the IP address, and the port number you are going to use to allow for communication.  Change
    the host to the IP address, the port to the port number you are using and the file_to_send to the location of the file
    you wish to send while leaving the r in front of the location.
'''

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))
file_to_send = r'F:\Download\test.txt'

f = open(file_to_send, 'rb')
print 'Sending...'
l = f.read(1024)
while (l):
    print 'Sending...'
    s.send(l)
    l = f.read(1024)
f.close()
print "Done Sending"
s.shutdown(socket.SHUT_WR)
print s.recv(1024)
s.close
