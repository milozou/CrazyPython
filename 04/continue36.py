#continue36.py
s = 0
for i in range(1,501):
    if i%36 != 0:
        continue
    print(i,end=" ")
    s+=1
