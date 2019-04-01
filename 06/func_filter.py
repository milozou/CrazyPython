#func_yeild.py
def f():
    print("one")
    yield 1
    print("two")
    yield 2
    print("three")
    yield 3
    print("four")

g = f()

print("#"*50)
gv = next(g)
print("next:",gv)

print("#"*50)
gv = next(g)
print("next:",gv)

print("#"*50)
gv = next(g)
print("next:",gv)

print("#"*50)
gv = next(g)
print("next:",gv)

print("#"*50)
