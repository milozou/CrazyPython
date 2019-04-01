#jcz.py

import jieba
import jieba.analyse

text = """
苏轼《江城子》
乙卯正月二十日夜记梦
十年生死两茫茫，不思量，自难忘。千里孤坟，无处话凄凉。纵使相逢应不识，尘满面，鬓如霜。
夜来幽梦忽还乡，小轩窗，正梳妆。相顾无言，唯有泪千行。料得年年肠断处，明月夜，短松岗。"""

# seg_list = jieba.cut(text, cut_all=False)  #精确模式（默认是精确模式）
seg_list = jieba.cut(text)
print("[精确模式]: ", "/ ".join(seg_list))

seg_list2 = jieba.cut(text, cut_all=True)    #全模式
print("[全模式]: ", "/ ".join(seg_list2))

seg_list3 = jieba.cut_for_search(text)       #搜索引擎模式
print("[搜索引擎模式]: ","/ ".join(seg_list3))

tags = jieba.analyse.extract_tags(text, topK=5)
print("[关键词]:", " / ".join(tags))
