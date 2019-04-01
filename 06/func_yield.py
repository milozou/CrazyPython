#func_yield.py
def f():
    print("one")
    yield 1
    print("two")
    yield 2
    print("three")

    
g = f()
gy = next(g)
print(gy)
gy = next(g)
print(gy)
gy = next(g)
print(gy)

