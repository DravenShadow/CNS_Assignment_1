"""
    Author:  Rowland DePree             Client.py

    This is a client designed to connect to a server file on a different computer.  To do this, you will need to know
    the server IP address and the port number that you are connecting to.  Changed those in the program in order to
    connect to the correct server and get back a time stamp of when you connected to the server.
"""
import socket


def main():
    """
    Main program
    :return:
    """
    s = socket.socket()
    host = socket.gethostname()
    port = 12345

    s.connect((host, port))
    print s.recv(1024)
    s.close


# Runs the main program
if __name__ == '__main__':
    main()
