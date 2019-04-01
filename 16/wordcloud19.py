#wordcloud19.py
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
 
filetext = open('libai.txt', encoding='utf8').read()
 
wordlist = jieba.cut(filetext, cut_all = True)
wl_space_split = " ".join(wordlist)
 
my_wordcloud = WordCloud(font_path="C:\WindowsFonts\simhei.ttf").generate(wl_space_split)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
