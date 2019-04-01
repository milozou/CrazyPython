#Show.py
def show(filename):
    dictList = []
    textdict = {}
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            dictList.append(line.split())

        print('%-10s%10s' % ('word', 'count'))
        print('-'*25)
        for k,v in dictList:
            if int(v) > 100:    #只显示频率大于100的词
                print('%-12s    %6s' % (k, v))

show("rlibai.txt")
