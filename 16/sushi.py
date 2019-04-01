#包含的库
import re
import urllib
import urllib.request

#自定义的保存函数，由于需要不断的打开文件、写入文件操作，效率很低。
def saveData(data, savePath):
    f = open(savePath, 'a')
    try:
        f.write(data)
    except:
        pass
    f.close()

cnt = 1 
#匹配笑话的正则表达式
rule_joke = r'<div class="summary">\r\n(*?)</div>'
save_path = 'qb_jokes.txt'
url_header = 'http://www.shicimingju.com/chaxun/zuozhe/9_%s.html'
url_tail = 2

while url_tail < 5:
    #由于糗事百科网页特殊性，直接改变页号即可实现访问不同网页
    url = url_header % str(url_tail)
    request = urllib.request.Request(url, headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)\
             Chrome/50.0.2657.3 Safari/537.36'
    })
    #尝试打开网页，读取信息
    try:
        html = urllib.request.urlopen(request)
        data = html.read()
    except:
        print('Parser Html Error!')
        continue
    #尝试匹配网页中的笑话
    jokes = re.compile(rule_joke)
    try:
        joke = jokes.findall(data.decode("UTF-8"))
    except:
        print("Find jokes error!\n")
        continue
    #将得到的笑话的字符串处理并存储
    for j in joke:
        print(str(cnt) + j + "\n")
        saveData(str(cnt) + j + "\n", save_path)
        cnt += 1
    #表示读取下一页
    url_tail += 1
