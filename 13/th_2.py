#th_2.py
import threading
class MyThread(threading.Thread):  
    def __init__(self,x,y):     #子类定义初始化方法
        threading.Thread.__init__(self)    #调用父类初始化方法
        self.x, self.y = x, y
    def run(self):    #重载run方法
        for i in range(self.y):
            print("输出 %s 共 %d 次"%(self.x, self.y))

t1 = MyThread("画面", 3)
t2 = MyThread("声音", 3)

t1.start()
t2.start()
