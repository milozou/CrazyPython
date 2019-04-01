#tcpserver.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 6000))
s.listen(10)
print('Waiting for connection...')

clients, clientaddr = s.accept()
data = clients.recv(1024)
print("client %s say: %s" % (clientaddr, data.decode()))

clients.send(b"hello, i am Server")
clients.close()
