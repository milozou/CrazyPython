#my_error_class.py
class MyError(Exception):
    def __init__(self, length, least):
        self.length = length
        self.least = least

if __name__ == "__main__":
    try:
        s = input("请输入一个字符串：")
        if len(s) > 5:
            raise MyError(len(s), 5)    #抛出自定义异常并传参
    except MyError as m:
        print("MyError: 输入长度为 %s ，长度不能超过 %d" % (m.length, m.least))
