#class_sc.py
class A:
    @staticmethod
    def sm():
        print("静态方法")

    @classmethod
    def cm(self):
        print("类方法")

a = A()
A.sm()
a.sm()
A.cm()
a.cm()
