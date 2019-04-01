import urllib.request
import re
def getHtml(url): 
    page = urllib.request.urlopen(url) 
    html = page.read() 
    page.close()
    #print(html)
    return html 

def getImg(html): 
    reg = 'src="(.*?\.jpg)" size' 
    imgre = re.compile(reg)
    weatherList = imgre.findall(html.decode()) 
    i = 0
    for imgurl in weatherList:
        print(imgurl)
        urllib.request.urlretrieve(imgurl, "%d.jpg"%(i,))
        i+=1

ht =  getHtml(r"https://tieba.baidu.com/p/5659540928")
getImg(ht)
