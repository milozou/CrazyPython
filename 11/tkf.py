#tkf.py
import tkinter
import turtle
root = tkinter.Tk()                     #生成主窗口
label = tkinter.Label(root,text="你好") #生成标签
label.pack()                            #将标签添加至主窗口
button1 = tkinter.Button(root,text="五角星")   #生成按钮
button1.pack()                          #将按钮添加至主窗口
####
def wjx(event):                         #事件响应函数
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
####
button1.bind('<Button-1>',wjx)          #绑定事件

root.mainloop()                         #进入消息循环
