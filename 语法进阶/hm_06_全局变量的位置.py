# 注意: 在开发时,应该模块中的所有全局变量
# 都定义在所有函数上方,就可以保证所有的函数
# 都能够正常的访问到每一个全局变量了
num = 10
title = "传智 - 黑马"
name = "小明"

def demo():
    print("%s" % num)
    print("%s" % title)
    print("%s" % name)

demo()