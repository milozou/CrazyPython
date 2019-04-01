#tk1.py
import tkinter
root = tkinter.Tk()    #生成主窗口
label = tkinter.Label(root, text="你好")    #生成标签对象
label.pack()    #将标签添加到主窗口
button1 = tkinter.Button(root, text="五角星")    #生成按钮
button1.pack()    #将按钮添加到主窗口
root.mainloop()
