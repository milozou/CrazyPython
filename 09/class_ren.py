#class_ren.py
class Ren:
    """这里是关于类的描述"""
    className = "Ren"
    def __init__(self, name='', money=0):
        self.name = name
        self.__money = money

    def say(self):
        """有必要的时候，这里是方法的说明"""
        print("I am %s ,i have %d yuan" % (self.name, self.__money))

#main
if __name__ == "__main__":
    milo = Ren()
    zqx = Ren("zouqixian", 100)
    print(Ren.className)
    milo.say()
    zqx.say()
    print(Ren.name)
