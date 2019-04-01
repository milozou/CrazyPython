#walkdir.py
import os
def walk(dirName):
    for name in os.listdir(dirName):
        path = os.path.join(dirName, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

walk('a')
