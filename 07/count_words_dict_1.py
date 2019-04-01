#count_words_dict_1.py
contents = open('KMSWHS.txt','r').read().lower()
cList = contents.split()

def histogram(contents):
    d = {}
    for w in contents:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    return d

def show(wordsDict):
    dictList = []
    for key, val in wordsDict.items():
        dictList.append((val, key))
    dictList.sort(reverse=True)         #倒序排序
    print('%-10s%10s' % ('word', 'count'))
    print('-'*25)
    for val,key in dictList:
        if val > 10:
            print('%-12s    %3d' % (key, val))
    
h = histogram(cList)
show(h)
