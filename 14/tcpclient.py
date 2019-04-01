#tcpclient.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 6000))
s.send(b"hello,i am client")

data = s.recv(1024)
print("server say: %s" % data.decode())
s.close()
