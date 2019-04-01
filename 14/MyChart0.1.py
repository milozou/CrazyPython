#MyChart0.1.py
import wx
import socket
import threading
import queue
import time
import random
import string

class MyChartFrame(wx.Frame):
    """GUI 模块"""
    def __init__(self, parent, title, size=(640,480)):
        """构造函数，初始化主要方法"""
        wx.Frame.__init__(self, parent, title=title, size=(640,480))

        #等待发送的消息的队列
        self.sendMsgQueue = queue.Queue(200)
        #生成将要给消息队列上的锁，用于保证同一时刻只有一个线程对队列操作
        self.sendMsgQueueLock = threading.Lock()

        self.initUI()
        self.bindEvent()
        self.startMsgThread()
        self.Show()

    def initUI(self):
        seed = "0123456789"
        randomName = "".join(random.sample(seed, 8))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)  #全局布局管理器

        #聊天记录组件及布局
        self.tcMsgAll = wx.TextCtrl(panel,
                                    style=wx.TE_READONLY|wx.TE_MULTILINE,
                                    size=(530, 300))
        vbox.Add((-1,15))   #增加窗口中的空白空间
        vbox.Add(self.tcMsgAll,proportion=1,
                 flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
                
    	#昵称组件及布局
        stName = wx.StaticText(panel, label='昵称')
        self.tcName = wx.TextCtrl(panel)
        self.tcName.SetValue(randomName)
        hboxName = wx.BoxSizer(wx.HORIZONTAL)  #昵称行管理器
        hboxName.Add(stName,
                    flag=wx.RIGHT|wx.ALIGN_CENTER_VERTICAL,border=10)
        hboxName.Add(self.tcName,
                    flag=wx.ALIGN_CENTER_VERTICAL)
        vbox.Add(hboxName,
                 flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=20)
        vbox.Add((-1,15))    #增加窗口中的空白空间
        
        #用户输入内容的文本框和发消息的按钮
        self.tcMsgEnt = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(500, 80))
        self.btnSendMsg = wx.Button(panel, label="发送")
        hboxMsgEnt = wx.BoxSizer(wx.HORIZONTAL)
        hboxMsgEnt.Add(self.tcMsgEnt, proportion=1,
                       flag=wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, border=10)
        hboxMsgEnt.Add(self.btnSendMsg,
                       flag=wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, border=5)
        vbox.Add(hboxMsgEnt, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=15)
        vbox.Add((-1,15))

        panel.SetSizer(vbox)    #启动布局管理器
        vbox.SetSizeHints(self)    #组件最小限制

    def btnEvtSendMsg(self,evt):
        """按钮事件处理"""
        n = self.tcName.GetValue()
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        m = self.tcMsgEnt.GetValue()
        msg = "%s %s :\n%s\n\n" % (n, t, m )
        self.tcMsgEnt.Clear()

        self.sendMsgQueueLock.acquire()    #获取消息队列锁
        self.sendMsgQueue.put(msg.encode('utf8'))    #向队列放入数据
        self.sendMsgQueueLock.release()    #释放消息队列锁

    def bindEvent(self):
        """绑定发送按钮事件"""
        self.btnSendMsg.Bind(wx.EVT_BUTTON, self.btnEvtSendMsg)

    def startMsgThread(self):
        """实例化接收和发送消息的模块，并启动线程"""
        self.recvMsgThread = RecvMsgThread(self) 
        self.sendMsgThread = SendMsgThread(self.sendMsgQueue, self.sendMsgQueueLock)
        self.recvMsgThread.start()
        self.sendMsgThread.start()

    def RefreshTcMsgAll(self, msg):
        """刷新聊天记录"""
        self.tcMsgAll.AppendText(msg)

    def __del__(self):
        """析构函数，程序结束时，结束线程"""
        self.recvMsgThread.stop()
        self.sendMsgThread.stop()
        self.recvMsgThread.join()
        self.sendMsgThread.join()

class SendMsgThread(threading.Thread):
    """消息发送模块"""
    def __init__(self, sendMsgQueue, sendMsgQueueLock):
        threading.Thread.__init__(self)
        self.threadName = "SendMsgThread"
        self.exitFlag = threading.Event()

        self.sendMsgQueue = sendMsgQueue
        self.sendMsgQueueLock = sendMsgQueueLock

    def run(self):
        group_ip = "224.1.1.1"    #组播地址
        port = 8000             #自定义端口
        print("starting ", self.threadName)    #在后台终端输出

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)

        #监视消息队列，一旦有消息就读取消息并发送，直到线程停止
        while not self.stopped():
            self.sendMsgQueueLock.acquire()  #获取队列锁
            if not self.sendMsgQueue.empty():
                msg = self.sendMsgQueue.get()  #读取队列消息
                self.sendMsgQueueLock.release()  #取得消息后释放队列锁
                s.sendto(msg, (group_ip, port))    
                print("%s sending %s" % (self.threadName, msg))
            else:
                self.sendMsgQueueLock.release()
            time.sleep(1)

        s.close()
        print("Exiting ", self.threadName)

    def stop(self):
        self.exitFlag.set()

    def stopped(self):
        return self.exitFlag.isSet()

class RecvMsgThread(threading.Thread):
    """消息接收模块"""
    def __init__(self, mainThread):
        threading.Thread.__init__(self)
        self.threadName = "RecvMsgThread"
        self.mainThread = mainThread
        self.exitFlag = threading.Event()

    def run(self):
        group_ip = "224.1.1.1"
        port = 8000

        print("starting ", self.threadName)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)

        s.bind(('', port))
        host = socket.gethostbyname(socket.gethostname())
        s.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(host))
        s.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP,
                        socket.inet_aton(group_ip) + socket.inet_aton(host))

        #从网络接收消息，接收到消息便显示，知道线程被停止
        while not self.stopped():
            try:
                msg, addr = s.recvfrom(1024)
                wx.CallAfter(self.mainThread.RefreshTcMsgAll, msg)
            except socket.error as e:
                print("receiving expection")
            time.sleep(1)

        s.close()
        print("Exiting ", self.threadName)

    def stop(self):
        self.exitFlag.set()

    def stopped(self):
        return self.exitFlag.isSet()



if __name__ == "__main__":
    app = wx.App()
    frame = MyChartFrame(None, title='Milo 的 局域网聊天室 V0.1')
    frame.Show(True)
    app.MainLoop()















