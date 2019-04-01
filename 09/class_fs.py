#class_fs.py
class A:
    name = "class A"

    def __init__(self):
        self.i = "init A"

    def a(self):
        print("function a")

class B:
    name = "class B"

    def __init__(self):
        self.i = "init B"

    def b(self):
        print("function b")

class C(A):
    name = "class C"
    pass

class D(B,A):
    pass

#main
c = C()
print("c.name",c.name)
print("c.i",c.i)
c.a()

d = D()
print("d.name",d.name)
print("d.i",d.i)
d.a()
d.b()

    
