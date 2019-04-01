#DataSplit.py
import os
import os.path

def dataSplit(sFile, dFolder):
    line = 2000    #每个文件保存行数
    datatemp = []    #缓存列表
    n = 1    #分割后的文件序号
    if not os.path.isdir(dFolder):    #判断目标目录是否存在
            os.mkdir(dFolder)         #创建目标目录
    with open(sFile, 'r', encoding='utf8') as sf:
        dataline = sf.readline()
        while dataline:    #判断是否从云文件读取到数据
            for row in range(line):    #读取100行
                datatemp.append(dataline)    #向缓存添加一行
                dataline = sf.readline()
                if not dataline:    #原文件读取不到数据时结束循环
                    break
            dfilename = os.path.join(dFolder,
                                     os.path.split(sFile)[1] +
                                     str(n) + ".txt")
        
            with open(dfilename, 'w', encoding='utf8') as df:
                df.writelines(datatemp)     #将缓存写入目标文件
                datatemp = []    #清空缓存
                print("%s 创建成功" % dfilename)
                n += 1
if __name__ == "__main__":
    dataSplit("libai.txt", "libai")

    
