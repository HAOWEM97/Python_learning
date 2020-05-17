def demo1():

    # 定义一个局部变量
    num = 10

    print("在demo1函数内部的变量是%d" % num)

def demo2():
    num = 99
    print("demo2 ==》%d" % num)


# 在函数内部定义的变量，不能在其他地方使用
# print("%d" % num)
demo1()
demo2()
