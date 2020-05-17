# 全部变量
num = 10


# 两个函数都可以使用全局变量num
def demo1():
    # 希望在demo1()修改全局变量 => 使用 global 声明一下变量即可
    # global关键字会告诉解释器后面的变量是一个全局变量
    # 再使用赋值语句时,就不会创建局部变量
    global num
    num = 99
    print("demo1 => %s" % num)

def demo2():
    print("demo2 => %s" % num)

demo1()
demo2()