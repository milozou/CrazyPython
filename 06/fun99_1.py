#fun99_1.py
def fun99(x):
    for i in range(1, x+1):
        for j in range(1, i+1):
            print(j, '*', i, '=', i*j, '\t', end='')
        print('\n')

print("It's Main")
x = fun99(3)
print(x)
