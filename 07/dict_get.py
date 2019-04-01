#dict_get.py
a = 1
b = 2
c = input('operator>')

def myAdd(x, y):
    return x + y

def mySubtract(x, y):
    return x - y

result = {  '+' : myAdd(a,b),
            '-' : mySubtract(a,b)
         }

print(result.get(c, "just '+、-'"))
