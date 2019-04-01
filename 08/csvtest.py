#csvtest.py
import csv
readObj = open('test.csv','rU')
csvobj = csv.reader(readObj)
allCsv = []
for row in csvobj:
    allCsv.append(row)

allCsv[1][3] = 70

theSum = 0
for i in allCsv[1][1:4]:
    theSum += int(i)
x = theSum/3
allCsv[1][-1] = '%d' % x

theSum = 0
for row in allCsv[1:-1]:
    theSum += int(row[-1])
y = theSum/3
allCsv[-1][-1] = y


with open('newtest.csv','w') as writeObj:
    writer = csv.writer(writeObj)
    for row in allCsv:
        writer.writerow(row)
