#try_file.py
try:
    f = open("test.txt", 'r')
    print(f.read())
except IOError:
    print("文件不存在")
finally:
    #f.close()
    try:
        f.close()
    except NameError:
        pass
    
