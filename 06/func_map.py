#func_map.py
l1 = [1, 2, 3]
l2 = [5, 7, 8, 11]

def func(x,y):
    return x+y

for i in (map(func, l1, l2)):
    print(i)
