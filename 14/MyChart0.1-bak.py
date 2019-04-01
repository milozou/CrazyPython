#MyChart0.1.py
import wx
import socket
import threading
import queue
import time
import struct
import random
import string

class MyChartFrame(wx.Frame):
    """GUI 模块"""
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(640,480))
        self.tcMsgEnt = None
        self.btnSendMsg = None
        self.tcMsgAll = None
        self.tcName = None

        #等待发送的消息的队列
        self.sendMsgQueue = queue.Queue(200)
        #生成将要给消息队列上的锁
        self.sendMsgQueueLock = threading.Lock()

        self.initUI()
        #self.bindEvent()
        #self.startMsgThread()

        self.Centre()
        self.Show()

    def initUI(self):
        seed = "0123456789"
        randomName = "".join(random.sample(seed, 4))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)  #全局布局管理器

        #聊天记录
        hboxMsgAll = wx.BoxSizer(wx.HORIZONTAL)
        self.tcMsgAll = wx.TextCtrl(panel, style=wx.TE_READONLY|wx.TE_MULTILINE, size=(530, 300))
        hboxMsgAll.Add(self.tcMsgAll, proportion=1,
                       flag=wx.LEFT|wx.RIGHT|wx.EXPAND,border=10)
        vbox.Add((-1,15))
        vbox.Add(hboxMsgAll,proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        vbox.Add((-1,15))
        
    	#昵称
        hboxName = wx.BoxSizer(wx.HORIZONTAL)  #昵称行管理器
        stName = wx.StaticText(panel, label='昵称')
        hboxName.Add(stName,
                    flag=wx.RIGHT|wx.ALIGN_CENTER_VERTICAL,border=10)
        self.tcName = wx.TextCtrl(panel)
        self.tcName.SetValue(randomName)
        hboxName.Add(self.tcName,
                    flag=wx.ALIGN_CENTER_VERTICAL)
        vbox.Add(hboxName,
                 flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=20)
        vbox.Add((-1,15))
        
        #用户输入内容的文本框和发消息的按钮
        hboxMsgEnt = wx.BoxSizer(wx.HORIZONTAL)
        self.tcMsgEnt = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(500, 80))
        hboxMsgEnt.Add(self.tcMsgEnt, proportion=1,
                       flag=wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, border=10)
        self.btnSendMsg = wx.Button(panel, label="发送")
        hboxMsgEnt.Add(self.btnSendMsg,
                       flag=wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, border=5
                       )
        vbox.Add(hboxMsgEnt, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=15)
        vbox.Add((-1,15))
        
        panel.SetSizer(vbox)
        vbox.SetSizeHints(self)    #启动组件最小限制


if __name__ == "__main__":
    app = wx.App()
    frame = MyChartFrame(None, title='Milo 的 局域网聊天室 V0.1')
    frame.Show(True)
    app.MainLoop()















