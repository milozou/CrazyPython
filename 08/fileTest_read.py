#fileTest_read.py
f = open("tmp.txt", 'r')
contents = f.read()
for line in contents:
    print('=>',line)
f.close()
