#fun99.py
def fun99():
    for i in range(1, 7):
        for j in range(1, i+1):
            print(j, '*', i, '=', i*j, '\t', end='')
        print('\n')

print("It's Main")
fun99()
