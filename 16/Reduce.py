#Reduce.py
import os
import os.path

def Reduce(sFolder, dFile):
    datatemp = {}
    for root,dirs,files in os.walk(sFolder):
        for f in files:
            if f.endswith(".map.txt"):
                with open(os.path.join(root,f),'r', encoding='utf8') as sf:
                    for line in sf:
                        #print(line)
                        k,v = line.split()
                        #print(line)
                        if k in datatemp:
                            datatemp[k] = int(datatemp[k]) + int(v)
                        else:
                            datatemp[k] = v
    dList = []
    for k,v in datatemp.items():
        dList.append(k + ' ' + ' ' + str(v) + '\n')
                                 
    with open(dFile, 'w', encoding='utf8') as df:
        df.writelines(dList)     #将缓存写入目标文件
        print("%s 合并成功" % dFile)

if __name__ == "__main__":
    Reduce("libai",'rlibai.txt')
