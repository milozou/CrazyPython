#th_1.py
import threading    #导入threading模块
def run(x,y):       
    for i in range(y):
        print("输出 %s 共 %d 次"%(x,y) )

#生成两个线程图t1和t2
t1 = threading.Thread(target = run, args = ("画面", 3))
t2 = threading.Thread(target = run, args = ("声音", 3))

#分别启动两个线程
t1.start()
#t1.join()
t2.start()
"""
run("画面",3)
run("声音",3)
"""
