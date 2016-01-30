import socket

s = socket.socket()
host = socket.gethostname()
port = 12345


def socket_string_transfer(send, info=''):
    recive_info = ''

    s.connect((host, port))
    if send:
        s.send(str(info))
        recive_info = 'Move Sent...'
    else:
        recive_info = s.recv(1024)
    s.shutdown(socket.SHUT_RDWR)
    s.close()

    return recive_info


def main():
    print socket_string_transfer(False)

    user_input = input('Enter in the location you want to place an X in: ')

    socket_string_transfer(True, user_input)


if __name__ == '__main__':
    main()
