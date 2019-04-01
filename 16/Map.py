#Map.py
import jieba
import os
import os.path
import re

def Map(sFile, dFolder):
    datatemp = {}
    if not os.path.isdir(dFolder):    #判断目标目录是否存在
        os.mkdir(dFolder)         #创建目标目录
    with open(sFile, 'r', encoding='utf8') as sf:
        datatext = sf.read()
        seg_list = jieba.cut(datatext)  # 精确模式（默认是精确模式）
    for w in seg_list:
        if w in datatemp:
            datatemp[w] += 1
        else:
            datatemp[w] = 1

    dList = []
    for k,v in datatemp.items():
        if not re.findall('[\n，、（）“”：！。《》\s]',  k):
            dList.append(k + ' ' + ' ' + str(v) + '\n')
    dfilename = os.path.join(dFolder,
                             os.path.split(sFile)[1] + ".map.txt")
    with open(dfilename, 'w', encoding='utf8') as df:
        df.writelines(dList)     #将缓存写入目标文件
        print("%s 处理完毕" % dfilename)
     
Map("libai\libai.txt1.txt",'libai')
Map("libai\libai.txt2.txt",'libai')
Map("libai\libai.txt3.txt",'libai')
Map("libai\libai.txt4.txt",'libai')
