# -*- coding: utf-8 -*-
import urllib.request
import urllib
import re

url = "http://www.qiushibaike.com/imgrank/"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
})
response = urllib.request.urlopen(req)
content = response.read().decode('utf-8')
print(content)
patternPic = re.compile('<a.*?>\n<img src="(.*?)".*?>')
pattern = re.compile('<div.*?class="content">.*?<span>(.*?)</span>.*?</a>'+'(.*?<div.*?"stats".*?</div>)', re.RegexFlag.S)
items = re.findall(pattern, content)
for item in items:
    print(item)
    print(isinstance(item, str))
    print()
    if re.search('img', item[1]):
        #再次匹配
        patternA = re.compile('<a.*?>.*?<img src="(.*?)".*?>', re.RegexFlag.S)
        img = patternA.findall(item[1])
        print('段子：==> '+item[0], '\n\n', '段子图片：==> '+img[0]+'\n\n\n')
    else:
        print('段子：==> '+item[0], '\n\n\n')
