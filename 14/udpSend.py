# udpSend.py
import socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    addr = ("192.168.122.1", 6000)
    s.sendto("Hello Python", addr)
~