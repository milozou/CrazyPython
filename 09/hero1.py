#hero2.py
#定义英雄和怪物的模板
def hero(name, hp, attack):
    def kill(h):
        print("hero %s attacking monster!" % h['name'])
        
    data = {
        'name':name,
        'hp':hp,
        'attack':attack,
        'kill':kill
    }

    return data
 
def monster(name, hp, monster_type):
    def walking(m):
        print("monster %s : Walking!"%m['name'])
        
    data = {
        'name':name,
        'hp':hp,
        'type':monster_type,
        'walking':walking
    }

    return data

hero2 = hero('mario', 100, 20)
monster1 = monster('turtle', 200, 'turtle')

"""
kill(hero2)
walking(monster1)
kill(monster1)
"""

hero2['kill'](monster1)

