#timeList.py
import time
startTime = time.time()
sum([i for i in range(1, 10000000) if i%3 ==0 or i%5 ==0])
endTime = time.time()
print("list:", endTime - startTime)

startTime = time.time()
sum((i for i in range(1, 10000000) if i%3 ==0 or i%5 ==0))
endTime = time.time()
print("generator:", endTime - startTime)
