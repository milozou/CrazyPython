#wxmychat-0.3.py
import wx
import time

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Milo Chat",size = (520,450))
        panel = wx.Panel(self)
        labelAll = wx.StaticText(panel,-1,'All Contents')
        self.textAll = wx.TextCtrl(panel,-1,
                                  size=(480,200),
                                  style=wx.TE_READONLY|wx.TE_MULTILINE)
        labelIn = wx.StaticText(panel,-1,'I Say')
        self.textIn = wx.TextCtrl(panel,-1,
                                 size=(480,100),
                                 style=wx.TE_MULTILINE) 
        self.btnSent = wx.Button(panel,-1,"Sent",size=(75,25))
        self.btnClear = wx.Button(panel,-1,"Clear",size=(75,25))
        self.Bind(wx.EVT_BUTTON,self.OnButtonSent,self.btnSent)
        self.Bind(wx.EVT_BUTTON,self.OnButtonClear,self.btnClear)
        ### 布局管理 ####
        btnSizer = wx.BoxSizer()    #创建横向管理器
        btnSizer.Add(self.btnSent,proportion=0)
        btnSizer.Add(self.btnClear,proportion=0)

        mainSizer = wx.BoxSizer(wx.VERTICAL)    #创建纵向管理器
        mainSizer.Add(labelAll,proportion=0,flag=wx.ALIGN_CENTER)
        mainSizer.Add(self.textAll,proportion=1,flag=wx.EXPAND)
        mainSizer.Add(labelIn,proportion=0,flag=wx.ALIGN_CENTER)
        mainSizer.Add(self.textIn,proportion=0,flag=wx.EXPAND)
        mainSizer.Add(btnSizer,proportion=0,flag=wx.ALIGN_CENTER)

        panel.SetSizer(mainSizer)
        mainSizer.SetSizeHints(self)    #启动组件最小限制
        ################
        
    def OnButtonSent(self,event):
        userinput = self.textIn.GetValue()
        self.textIn.Clear() 
        nowtime = time.ctime()
        inmsg = "You (%s) :\n%s \n" % (nowtime,userinput)
        self.textAll.AppendText(inmsg)  #尾部添加文本
        
    def OnButtonClear(self,event):
        self.textall.Clear() 

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()      
