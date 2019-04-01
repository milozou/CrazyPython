#th_name.py
import threading
class MyThread(threading.Thread):  
    def __init__(self,threadName):     
        threading.Thread.__init__(self, name=threadName)
        
t1 = MyThread("画面")
print(t1.getName())
t1.setName('声音')
print(t1.getName())
