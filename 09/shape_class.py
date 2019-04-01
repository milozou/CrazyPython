#shape_class.py
class Square:
    def perimeter(self):
        raise AttributerError("子类须重载此方法，否则抛出这个异常")

class Triangle(Square):
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z
    def perimeter(self):
        print(self.a + self.b + self.c)

class Shape(Square):
    def __init__(self, x):
        self.x = x
    def perimeter(self):
        print(self.x * 4)

#main
triangle1 = Triangle(3,4,5)
shape1 = Shape(9)

triangle1.perimeter()
shape1.perimeter()
