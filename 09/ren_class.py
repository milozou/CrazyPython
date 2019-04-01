#class_ren.py
class Ren:
    className = "Ren"
    def __init__(self, name='', money=0):
        self.name = name
        self.__money = money

    def say(self):
        print("I am %s ,i have %d yuan" % (self.name, self.__money)

#main
#if __name__ == "__main__":
milo = Ren()
zqx = Ren("zouqixian", 100)
print(Ren.name)
milo.say()
zqx.say()
