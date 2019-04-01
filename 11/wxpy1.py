#wxpy1.py   #对象化生成空白窗口
import wx
app = wx.App()                  #应用程序对象
frame = wx.Frame(parent = None) #框架窗口对象
frame.Show()                    #显示框架窗口
app.MainLoop()                  #进入消息循环
