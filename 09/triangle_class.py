#triangle_class.py
class Triangle:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z
    def perimeter(self):
        return self.a + self.b + self.c

#main
t1 = Triangle(3,4,5)
t2 = Triangle(9,9,9)
print("直角三角形周长=", t1.perimeter())
print("等边三角形周长=", t2.perimeter())
