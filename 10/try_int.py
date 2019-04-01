#try_int
def toInt(x):
    try:
        i = int(x)
    except BaseException as err:
        i = err
    return i

print(toInt('abc'))
print(toInt("123"))
print(toInt([456]))
