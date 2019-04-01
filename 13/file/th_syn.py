#th_syn.py
import threading
import time
class MyThread(threading.Thread):  
    def run(self):
        global x_db
        lock.acquire()
        x_db += 1
        time.sleep(5)
        print(x_db)
        lock.release()
lock = threading.Lock()

x_db = 0
t5 = []

for i in range(5):
    tn = MyThread()
    t5.append(tn)

for j in t5:
    j.start()
        
        

