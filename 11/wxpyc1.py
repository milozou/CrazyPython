#wxpyc1.py
import wx
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None) #生成框架窗口
        frame.Show()                    #显示框架窗口
        return True
app = MyApp()
app.MainLoop()      
