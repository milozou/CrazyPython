#!/usr/bin/python
#th_ping.py
from threading import Thread
import subprocess
from queue import Queue

queue5 = Queue()
ips = ['10.0.2.11',
       '10.0.2.12',
       '10.0.2.13',
       '10.0.2.14',
       '10.0.2.15']

def pinger(i, q):
    while True:
        ip = q.get()    #从队列中取出一个元素
        print("Thread %s : Pinging: %s " % (i, ip))
        """linux
        ret = subprocess.call('ping -c 1 %s' % ip,
                                shell=True,
                                stdout=open('/dev/null', 'w'),
                                stderr=subprocess.STDOUT)
        """
        #windows
        ret = subprocess.call('ping -c 1 %s' % ip,
                              shell=True,
                              stdout=open('NUL', 'w'),
                              stderr=subprocess.STDOUT)
        if ret == 0:
            print('%s : is alive' % ip)
        else:
            print('%s : did not respond' % ip)
        q.task_done() #占位，在完成一项任务之后，向任务已经完成的队列发送一个信号

for i in range(3):
    th = Thread(target=pinger, args=(i, queue5))
    th.setDaemon(True)    #设置daemon属性weiTrue，
    th.start()

for ip in ips:
    queue5.put(ip)   #向对列添加元素

print("Main Thread waiting.....")
queue5.join()    #阻塞调用线程，直到队列中的所有任务被处理掉
print('Done')
