import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))
file_to_send = r'C:\Users\depre\Pictures\images.jpg'

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
