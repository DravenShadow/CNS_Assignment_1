"""
    Author:  Rowland DePree             Client_Transport_Files.py

    This is a client design to receive a file from the server.  To do this, you will need to know the server IP address
    and the port number of the server.  Change the host name to the IP address of the server and the port number of the
    server as well.  You will also need to know what kind of file you are receiving.  Then change the file format in the
    name of the file you will be writing to match that file format you are receiving from.
"""

import socket


def main():
    """
    Main program
    :return:
    """
    s = socket.socket()
    host = '192.168.1.7'
    port = 12345

    s.connect((host, port))
    print 'Connected.'
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


# Runs the main program
if __name__ == '__main__':
    main()
