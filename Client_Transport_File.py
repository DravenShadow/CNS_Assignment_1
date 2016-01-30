'''
    Author:  Rowland DePree             Client_Transport_Files.py

    This is a client design to receive a file from the server.  To do this, you will need to know the server IP address
    and the port number of the server.  Change the host name to the IP address of the server and the port number of the
    server as well.  You will also need to know what kind of file you are receiving.  Then change the file format in the
    name of the file you will be writing to match that file format you are receiving from.
'''
import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
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
