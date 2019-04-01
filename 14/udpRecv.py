# udpRecv.py
import socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    addr = ("192.168.122.1", 6000) #本机IP地址和端口
    s.bind(addr)
    data, addr = s.recvfrom(1024) # 1024是缓存数据，单位是bytes
    print(data)