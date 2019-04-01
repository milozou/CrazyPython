#class_pp.py
class Triangle:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z
    @property    
    def perimeter(self):
        return self.a + self.b + self.c

t = Triangle(6,6,6)
print(t.perimeter)
