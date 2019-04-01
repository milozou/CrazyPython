#game/play.py
from heroes import *
msg =" 欢迎来到 英雄无敌的世界…………！"
if __name__ == "__main__":
    print(msg)
    milo = Hero('milo')       #实例化英雄（2）
    boss = Element('boss')    #实例化敌人（3）
    print("boss hp:",boss.hp) #显示敌人的HP(4)
    print("英雄发起攻击！")
    milo.hit(boss)            #英雄调用hit方法攻击boss对象(5)
    print("boss hp:",boss.hp) #显示敌人的HP(4)
