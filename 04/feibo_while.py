#feibo_while.py
a = 0
b = 1
i = 0
num = int(input())
while i < num:
    print(a)
    a, b = b, a+b    #核心算法
    i += 1
