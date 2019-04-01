#sk_AppleOrange.py
from sklearn import tree 
"""
features = [[150, 'bumpy'],
            [170, 'bumpy'],
            [130, 'smooth'],
            [140, 'smooth']]
"""
features = [[150, 0],[170, 0],[130, 1],[140, 1]]
labels = [1, 1, 0, 0]
clf = tree.DecisionTreeClassifier()     #生成决策树分类器
clf = clf.fit(features, labels)     #训练分类器
print(clf.predict([[160,0]]))

