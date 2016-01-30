'''
    Author:  Rowland DePree             Server_Transport_Files.py

    This is a server file design to send a file from the server to the client file.  To do this you will need to know the
    path of the file location, the IP address, and the port number you are going to use to allow for communication.  Change
    the host to the IP address, the port to the port number you are using and the file_to_send to the location of the file
    you wish to send while leaving the r in front of the location.
'''
import socket

s = socket.socket()
host = '173.67.178.110'
port = 27014
s.bind((host, port))
f = open('received_file.txt', 'wb')
s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    print "Receiving..."
    l = c.recv(1024)
    while (l):
        print "Receiving..."
        f.write(l)
        l = c.recv(1024)
    f.close()
    print "Done Receiving"
    c.send('Thank you for connecting')
    c.close()
