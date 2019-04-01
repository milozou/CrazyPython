#func_var2.py
x = 10

def func(i):
    global x, y
    print("x = ", i)
    x = 100
    y = 50
    
    print("local x =", x)
    print("local y =", y)

func(x)
print("x = ", x)
print("y = ", y)
