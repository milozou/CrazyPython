#wxwjxb.py
import wx
import turtle
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None,
                         title = "Milo's  Tool") #生成框架窗口
        panel = wx.Panel(frame,-1)               #生成面板
        self.buttonWJX = wx.Button(panel,-1,"五角星",pos=(50,50))
        self.Bind(wx.EVT_BUTTON,self.OnButtonWJX,self.buttonWJX)
        frame.Show()                            #显示框架窗口
        #return True

    def OnButtonWJX(self,event):
        for i in range(5):
            turtle.forward(100)
            turtle.right(144)

app = MyApp()
app.MainLoop()      
