#class_add.py
class MyList:
    
    def __init__(self, *args):
        self.__myList = []
        for arg in args:
            self.__myList.append(arg)

    def __add__(self, x):
        """当对象通过 + 符号对后面数字运算就会调用此方法"""
        for i in range(len(self.__myList)):
            self.__myList[i] = self.__myList[i] + x

    def show(self):
        print(self.__myList)

#main
l = MyList(1,2,3,4,5,6,7,8,9,10)
l.show()
l + 10
l.show()
