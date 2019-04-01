#count_words_dict_2.py
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

h = histogram(cList)
print(h)
