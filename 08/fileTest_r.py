#fileTest_r.py
f = open("tmp.txt", 'r')
for line in f:
    print('=>',line)
f.close()
