'''
Heroes beta-0.2
milo  str worldMap if while
'''
welcome = '-*-welcome to Heroes world!-*-'
mapmsg = '#######'
mapins = "\n-*- the world is like this -*-\n %s \n the '*' is you " % (mapmsg,)
worldMap = ['#','#','#','#','#','#','#']
instruction = '''
contrl your hero:| 'a'for left | 'd' for right |'''

print(welcome)

name = input('input your name:')
hp = 100

if not name:
    name = 'player01'

usermsg = {'name':name,'hp':hp}

print("HI£¡", usermsg['name'],'You Hp is :',usermsg['hp'])
print(mapins,instruction)

point = 0
while 1:
    worldMap[point] = "*"
    print('you are here',"".join(worldMap))
    userinput = input('go or quit:')

    if userinput == 'd' and point < 6:
        worldMap[point] = '#'
        point +=1
    elif userinput == 'a' and point > 0:
        worldMap[point] = '#'
        point -=1
    elif userinput == 'quit':
        print("goodbey!!")
        break
    else:
        print(instruction)
