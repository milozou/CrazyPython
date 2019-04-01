#func_machine_x.py
def machine(money, food="套餐", other=""):
    if not other:
        print("一份 %d 元 %s" % (money, food))
    else:
        print("一份 %d 元 %s 外加 %s" % (money, food, other))
#machine(money=30, other="可乐")
machine(100, "披萨", "可乐", "橙汁", "苏打水")
