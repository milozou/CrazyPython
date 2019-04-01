#raise_exception
s = "123456"
try:
    if len(s) >5:
        #raise Exception
        raise Exception("超过5个字符")
except Exception as err:
    print(err)

