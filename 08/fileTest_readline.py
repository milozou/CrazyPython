#fileTest_readline.py
f = open("wtmp.txt", 'r')
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
for line in f:
    print('=>',line)
f.close()
