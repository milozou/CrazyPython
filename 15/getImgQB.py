#getImgQB.py
from urllib import request
import re

url = "http://www.qiushibaike.com/imgrank/"
user_agent = 'Chrome/4.0 (compatible; MSIE 5.5; Windows NT)'

def getHtml(url):
    req = request.Request(url, headers={'User-Agent':user_agent})
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    #print(html)     #测试代码
    response.close()
    return html

def getImg(html):
    patternImg = re.compile('<a.*?>\n<img src="(.*?)".*?>')
    jpglist = re.findall(patternImg, html)
    i = 0
    for item in jpglist:
        patternJpeg = re.compile('.*\.jpe{0,1}g', re.I)
        #print(patternJpeg.findall(item))    #测试代码
        if patternJpeg.findall(item):
            #print("http:"+item)    #测试代码
            #异常处理作用是防止无效地址导致下载失败
            try:
                request.urlretrieve("http:"+
                                    patternJpeg.findall(item)[0],
                                    "%d.jpg" % i)
            except:
                pass
        i += 1
        
html = getHtml(url)
getImg(html)
