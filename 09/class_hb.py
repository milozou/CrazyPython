#class_hb.py
class Human:
    name = ''
    __money = 0

    def __init__(self, name, money):    
        self.name = name
        self.__money = money
        
    def show(self):
        print(self.name)
        print(self.__money)

class Baby(Human):    #继承human类
    __height = 0      #子类新定义的属性
    __weight = 0
    __sex = ""

    def __init__(self, name, money, height, weight, sex):    #重载__init__方法
        self.__height = height    #子类对象的新属性
        self.__weight = weight
        self.__sex = sex
        Human.__init__(self, name, money) #子类中调用父类方法

    def show(self):
        Human.show(self)    #调用父类方法
        print(self.__height)
        print(self.__weight)
        print(self.__sex)

#main        
x = Baby("milo", 100, 8, 60, "male")
x.show()
