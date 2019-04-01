#feibo_for.py
numList = [0,1]
num = int(input())
for i in range(num - 2):
    numList.append(numList[-2] + numList[-1])

print(numList)
